import xmlschema
from faker import Faker
import os
import random
import pycountry
from datetime import datetime, timedelta
from lxml import etree
from orienteering_startlist_screen import config


def _iso(dt: datetime) -> str:
    """
    Formats datetime into ISO-8601 format. If a tzinfo is given, it will be isoformat(), else tzinfo without offset
    YYYY-MM-DDTHH:MM:SS
    """
    if dt is None:
        return ""
    if dt.tzinfo:
        # datetime.isoformat() brings e.g. "2025-09-22T09:00:00+02:00"
        return dt.isoformat()
    else:
        return dt.strftime("%Y-%m-%dT%H:%M:%S")


def generate_individual_startlist_xml(num_classes: int = 4,
                           participants_per_class: int = 10,
                           global_start_time: datetime = datetime.now().replace(second=0, microsecond=0),
                           interval_seconds: int = 60,
                           class_spacing_seconds: int = 0,
                           xsd_file_path: str = "./src/orienteering_startlist_screen/resources/iof_v3_0.xsd",
                           out_path: str = "./example_generated.xml") -> str:
    fake = Faker()

    nsmap = {
        None: "http://www.orienteering.org/datastandard/3.0",  # Default namespace
        "xsi": "http://www.w3.org/2001/XMLSchema-instance"
    }

    root = etree.Element(
        "StartList",
        nsmap=nsmap,
        iofVersion="3.0",
        createTime=_iso(datetime.now()),
        creator=f"{config.application_name} / {config.organization_name}",
    )

    last_start_datetime = (num_classes * class_spacing_seconds) + (interval_seconds * (participants_per_class -1))
    end_datetime = global_start_time + timedelta(seconds=last_start_datetime)

    event = etree.SubElement(root, "Event")
    etree.SubElement(event, "Name").text = "Test-Event"
    start_time_el = etree.SubElement(event, "StartTime")
    etree.SubElement(start_time_el, "Date").text = global_start_time.strftime("%Y-%m-%d")
    etree.SubElement(start_time_el, "Time").text = global_start_time.strftime("%H:%M:%S")
    end_time_el = etree.SubElement(event, "EndTime")
    etree.SubElement(end_time_el, "Date").text = end_datetime.strftime("%Y-%m-%d")
    etree.SubElement(end_time_el, "Time").text = end_datetime.strftime("%H:%M:%S")

    person_id = 0
    entry_id = 1000
    bib_number = 99
    control_card = 8000000
    club_id = 10
    for class_index in range(num_classes):
        classes_el = etree.SubElement(root, "ClassStart")
        class_el = etree.SubElement(classes_el, "Class")
        etree.SubElement(classes_el, "StartName").text = f"Start {random.choice([1, 2])}"
        etree.SubElement(class_el, "Id").text = str(class_index)
        class_name = f"{random.choice(["Men", "Women"])}"
        class_name_short = class_name[0]
        etree.SubElement(class_el, "Name").text = f"{class_name}-{class_index}"
        etree.SubElement(class_el, "ShortName").text = f"{class_name_short}-{class_index}"

        class_base_start = global_start_time + timedelta(seconds=class_index * class_spacing_seconds)

        for person_index in range(participants_per_class):
            person_id += 1
            entry_id += 1
            bib_number += 1
            club_id += 1
            control_card += 1

            person_start_el = etree.SubElement(classes_el, "PersonStart")
            etree.SubElement(person_start_el, "EntryId").text = str(entry_id)

            person_el = etree.SubElement(person_start_el, "Person")
            etree.SubElement(person_el, "Id").text = str(person_id)
            person_start_name_el = etree.SubElement(person_el, "Name")
            etree.SubElement(person_start_name_el, "Family").text = fake.last_name()
            etree.SubElement(person_start_name_el, "Given").text = fake.first_name()

            club_el = etree.SubElement(person_start_el, "Organisation")
            etree.SubElement(club_el, "Id").text = str(club_id)
            etree.SubElement(club_el, "Name").text = f"{random.choice(['TSV', 'OLG', 'SV', 'SC'])} {fake.city()}"
            country_name = fake.country()
            try:
                country_obj = pycountry.countries.lookup(country_name)
                country_code3 = country_obj.alpha_3
            except LookupError:
                country_code3 = "XXX"  # Fallback
            etree.SubElement(club_el, "Country", code=country_code3).text = country_name

            start_el = etree.SubElement(person_start_el, "Start")
            etree.SubElement(start_el, "BibNumber").text = str(bib_number)
            person_start_time = class_base_start + timedelta(seconds=person_index * interval_seconds)
            etree.SubElement(start_el, "StartTime").text = _iso(person_start_time)
            etree.SubElement(start_el, "ControlCard").text = str(control_card)

    xml_bytes = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="utf-8")
    with open(out_path, "wb") as f:
        f.write(xml_bytes)

    if not os.path.isfile(xsd_file_path):
        raise FileNotFoundError(f"XSD file not found: {xsd_file_path}")

    schema = xmlschema.XMLSchema(xsd_file_path)
    schema.validate(xml_bytes)
    abs_path = os.path.abspath(out_path)
    print(f"XML schema validated: {xsd_file_path}")
    print(f"XML generated: {abs_path}")
    return abs_path
