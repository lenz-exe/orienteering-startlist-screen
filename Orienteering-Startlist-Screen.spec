# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\orienteering_startlist_screen\\main.py'],
    pathex=['./src/orienteering_startlist_screen'],
    binaries=[],
    datas=[('pyproject.toml', '.')],
    hiddenimports=['pyttsx4.drivers', 'pyttsx4.drivers.dummy', 'pyttsx4.drivers.espeak', 'pyttsx4.drivers.nsss', 'pyttsx4.drivers.sapi5', 'orienteering_startlist_screen.resources_rc'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt', 'notebook', 'torch', 'tensorflow', 'bokeh', 'llvmlite', 'babel', 'pyarrow', 'scipy', 'pandas', 'sphinx', 'sklearn', 'netCDF4', 'jedi', 'h5py', 'ttk', 'docutils', 'tcl8', 'sqlalchemy', 'simplejson', 'bcolz', 'numcodecs', 'numba', 'zmq', 'IPython', 'cytoolz', 'psutil', 'fastparquet', 'thrift', 'bson', 'snappy', 'markupsafe', 'tornado', 'pygame', 'tkinter', 'tcl', 'osgeo', 'matplotlib'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Orienteering-Startlist-Screen',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['src\\orienteering_startlist_screen\\resources\\images\\logo.ico'],
    contents_directory='.',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Orienteering-Startlist-Screen',
)
