PLUGIN_NAME = "Get Multi-value Subset"
PLUGIN_AUTHOR = "Joel Lintunen"
PLUGIN_DESCRIPTION = """Returns a subset of values from a multi-value tag.
<br /><br />
Examples:
<ul>
  <li><i>$getmultirange(catalognumber,0)</i> returns the first value if it exists</li>
  <li><i>$getmultirange(writer,2:4,\, )</i> returns the third and fourth values if they exist, separated by a
      comma</li>
</ul>
Arguments:
<ol>
  <li>Multi-value tag.</li>
  <li>List index or slicer. For example <i>"0"</i>, <i>":2"</i>, <i>"::2"</i> or <i>"-1"</i>.</li>
  <li>Separator which will be used to divide the values. The default is <i>"; "</i>.</li>
</ol>
"""
PLUGIN_VERSION = "1.0.0"
PLUGIN_API_VERSIONS = ["2.0", "2.1", "2.2"]
PLUGIN_LICENSE = "GPL-2.0"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-2.0.html"

from picard.metadata import MULTI_VALUED_JOINER
from picard.script import (
    normalize_tagname,
    register_script_function)


def func_get_multi_range(parser, multi, range, separator=MULTI_VALUED_JOINER):
    # Check inputs to prevent crashes on the options page
    if not multi or not range or not all(x.isdigit() or x in [':', '-', '+'] for x in range):
        return ""

    multi_values = parser.context.getall(normalize_tagname(multi))
    try:
        # Check if range is an index instead of a slicer
        if len(range.split(':')) == 1:
                return multi_values[int(range)]
        return separator.join(eval("{0}[{1}]".format(multi_values, range)))
    except (IndexError, SyntaxError, ValueError):
        return ""


register_script_function(func_get_multi_range, "getmultirange")

