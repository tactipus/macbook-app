# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:\\GitHub\\macbook-app\\main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    Tree('D:\\GitHub\\macbook-app\\'),
    a.scripts,
    a.binaries,
    a.datas,
    [],
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    name='macbook-pro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
