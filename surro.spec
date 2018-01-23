# -*- mode: python -*-

block_cipher = None


a = Analysis(['surro/__main__.py'],
             pathex=['.'],
             binaries=[],
             datas=[('songs/*.wav', 'songs'), ('assets/*.wav', 'assets')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['PySide', 'PyQt4', 'PyQt5', 'matplotlib'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='surro',
          debug=False,
          strip=True,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon='./assets/logo.ico')
