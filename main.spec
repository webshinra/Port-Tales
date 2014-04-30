# -*- mode: python -*-
a = Analysis(['main.py'],
             pathex=['C:\\Users\\Vincent\\Downloads\\Programming\\stunJam'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          Tree('data', prefix='data'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
