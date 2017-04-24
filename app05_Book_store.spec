# -*- mode: python -*-

block_cipher = None


a = Analysis(['app05_Book_store.py'],
             pathex=['/Users/alan/PycharmProjects/Python_Basic'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
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
          name='app05_Book_store',
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='app05_Book_store.app',
             icon=None,
             bundle_identifier=None)
