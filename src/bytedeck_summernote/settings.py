from django_summernote.settings import ALLOWED_TAGS, STYLES

# Extend a list of allowed tags (mandatory for ByteDeck project),
ALLOWED_TAGS += [
    # allow extra tags, fix #1340
    "pre",
    "kbd",
    "var",
    "mark",
    "small",
    "ins",
    "del",
    "samp",
    "font",
    "iframe",
    "hr",
    "figure",
    "figcaption",
    "address",
    "dl",
    "dt",
    "dd",
    # Bootstrap Blockquotes
    "footer",
    "cite",
    # HTML5 media
    "video",
    "audio",
    "source",
    "track",
    # MathML (mandatory for ByteDeck project)
    "math",
    "maction",
    "menclose",
    "merror",
    "mfenced",
    "mfrac",
    "mglyph",
    "mi",
    "mlabeledtr",
    "mmultiscripts",
    "mn",
    "mo",
    "mover",
    "mpadded",
    "mphantom",
    "mroot",
    "mrow",
    "ms",
    "mspace",
    "msqrt",
    "mstyle",
    "msub",
    "msup",
    "msubsup",
    "mtable",
    "mtd",
    "mtext",
    "mtr",
    "munder",
    "munderover",
    "none",
    "mprescripts",
    "semantics",
    "annotation",
    "annotation-xml",
]

# Extend a list of allowed CSS properties (mandatory for ByteDeck project),
STYLES += [
    # allow extra styles, fix #1340
    "float",
    "height",
    "list-style",
    "list-style-type",
    "margin-left",
    "margin-right",
    "text-align",
    "text-decoration",
    "text-indent",
    "width",
]
