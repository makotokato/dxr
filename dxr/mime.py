from os.path import splitext


def icon(path):
    """Return the basename (no extension) of the icon file to use for a path."""
    root, ext = splitext(path)
    return ext_map.get(ext[1:], 'unknown')


def is_text(data):
    # Simple stupid test that apparently works rather well :)
    return '\0' not in data


def is_binary_image(path):
    """Return whether the path points to an image without human-readable
    contents."""
    return icon(path) == 'image'


def is_textual_image(path):
    """Return whether the path points to an image with text contents."""
    return icon(path) == 'svg'


# File extension known as this point
ext_map = {
    "html":       'html',
    "xhtml":      'html',
    "htm":        'html',
    "js":         'js',
    "h":          'h',
    "hpp":        'h',
    "cpp":        'cpp',
    "cc":         'cpp',
    "cxx":        'cpp',
    "c":          'c',
    "xul":        'ui',
    "svg":        'svg',
    "SVG":        'svg',
    "in":         'build',
    "idl":        'conf',
    "java":       'java',
    "xml":        'xml',
    "py":         'py',
    "css":        'css',
    "mk":         'build',
    "txt":        'txt',
    "sh":         'sh',
    "ini":        'conf',
    "properties": 'conf',
    "dtd":        'xml',
    "patch":      'diff',
    "asm":        'asm',
    "jsm":        'js',
    "cfg":        'conf',
    "m4":         'conf',
    "webidl":     'conf',
    "vcproj":     'vs',
    "vcxproj":    'vs',
    "xsl":        'xml',
    "hxx":        'h',
    "sln":        'vs',
    "diff":       'diff',
    "cs":         'cs',
    "iso":        'iso',
    "php":        'php',
    "rb":         'rb',
    "ipdl":       'conf',
    "mm":         'mm',
    "tex":        'tex',
    "vsprops":    'vs',
    "jpg":        'image',
    "jpeg":       'image',
    "png":        'image',
    "gif":        'image'
}
