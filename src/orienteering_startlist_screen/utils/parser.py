import xmlschema
import os
import uuid
from datetime import datetime
from typing import Any, Dict, List, cast
import logging

from orienteering_startlist_screen.utils.own_dataclasses import Participant

logger = logging.getLogger(__name__)


def validate_iof_xml_3_0(xml_file_path: str, xsd_file_path: str) -> bool:
    try:
        if not os.path.isfile(xml_file_path):
            logger.error(f"XML file could not be found: {xml_file_path}")
            raise FileNotFoundError(f"XML file not found: {xml_file_path}")
        if not os.path.isfile(xsd_file_path):
            logger.error(f"XSD file could not be found: {xsd_file_path}")
            raise FileNotFoundError(f"XSD file not found: {xsd_file_path}")

        schema = xmlschema.XMLSchema(xsd_file_path)
        is_valid = schema.is_valid(xml_file_path)
        if is_valid:
            logger.info(
                f"XML file '{xml_file_path}' is valid against XSD '{xsd_file_path}'"
            )
        else:
            logger.info(
                f"XML file '{xml_file_path}' is not valid against XSD '{xsd_file_path}'"
            )
        return is_valid
    except xmlschema.XMLSchemaException as e:
        logger.error(f"XML validation failed: {e}")
        raise xmlschema.XMLSchemaException(e)
    except Exception as e:
        raise Exception(e)


def pars_participants_iof_xml_3_0(
    xml_file_path: str, xsd_file_path: str
) -> dict[str, dict[datetime, List[Participant]]]:
    try:
        validate_result = validate_iof_xml_3_0(xml_file_path, xsd_file_path)
        if not validate_result:
            raise Exception(
                f"XML file '{xml_file_path}' is not valid against XSD '{xsd_file_path}'"
            )
    except Exception as e:
        logger.error(
            f"Parsing IOF XML 3.0 failed. XML: {xml_file_path} | XSD: {xsd_file_path}"
        )
        logger.error(str(e))
        raise Exception(
            f"Parsing IOF XML 3.0 failed. XML: {xml_file_path} | XSD: {xsd_file_path}\n Exception: {e}"
        )
    random_start_name = f"undefined_start_name_{uuid.uuid4()}"
    try:
        # Load the schema
        schema = xmlschema.XMLSchema(xsd_file_path)
        # Parse the XML file (may return dict, tuple, or None depending on validation mode)
        raw = schema.to_dict(xml_file_path)

        # Normalize to a dict for safe `.get(...)`
        if raw is None:
            xml_dict: Dict[str, Any] = {}
        elif isinstance(raw, tuple):
            data, errors = raw  # type: ignore[misc]
            # You could log `errors` here if you want
            xml_dict = cast(Dict[str, Any], data or {})
        elif isinstance(raw, dict):
            xml_dict = cast(Dict[str, Any], raw)
        else:
            # Fallback: treat as empty dict (or raise)
            xml_dict = {}

        start_list: dict[str, dict[datetime, List[Participant]]] = {}
        for index, class_start in enumerate(xml_dict.get("ClassStart", []), start=1):
            if class_start.get("StartName"):
                start_name = class_start["StartName"][0]
            else:
                start_name = random_start_name
            class_name = class_start.get("Class", {}).get("Name")
            class_name_short = class_start.get("Class", {}).get("ShortName")

            if not start_list.get(start_name):
                start_list.setdefault(start_name, {})

            for person in class_start.get("PersonStart", []):
                first_name = person.get("Person", {}).get("Name", {}).get("Given")
                last_name = person.get("Person", {}).get("Name", {}).get("Family")
                club_name = person.get("Organisation", {}).get("Name")
                club_name_short = person.get("Organisation", {}).get("ShortName")
                country = person.get("Organisation", {}).get("Country", {}).get("$")
                country_short = (
                    person.get("Organisation", {}).get("Country", {}).get("@code")
                )
                tmp_start_time = person.get("Start", [])[0].get(
                    "StartTime", "2000-01-01T00:00:00+00:00"
                )
                start_time = datetime.fromisoformat(tmp_start_time)
                bib_number = person.get("Start", [])[0].get("BibNumber")
                if person.get("Start", [])[0].get("ControlCard", []):
                    control_card = person.get("Start", [])[0].get("ControlCard", [])[0]
                else:
                    control_card = None
                participant = Participant(
                    last_name=last_name,
                    first_name=first_name,
                    control_card=control_card,
                    club_name=club_name,
                    club_name_short=club_name_short,
                    class_name=class_name,
                    class_name_short=class_name_short,
                    country=country,
                    country_short=country_short,
                    start_time=start_time,
                    bib_number=bib_number,
                )

                if not start_list[start_name].get(start_time):
                    start_list[start_name].setdefault(start_time, [])
                start_list[start_name][start_time].append(participant)

        return start_list
    except Exception as e:
        logger.error(f"Error during parsing xml: {e}")
        raise Exception(f"Error during parsing xml: {e}")
