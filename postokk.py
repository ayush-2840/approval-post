import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))