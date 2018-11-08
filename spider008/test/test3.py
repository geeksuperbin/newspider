import re


s = '''// Save default language   $CONFIG[\'lang\'] = strtr($USER[\'lang\'], \'$/\\:\*?&quot;\\'&amp;lt;&gt;|`\', \'____________\');   }   elseif ($CONFIG[\'charset\'] == \'utf-8\') &amp;lt;== default configuration   {   include(\'include/select_lang.inc.php\');   if (file_exists(\'lang/\' . $USER[\'lang\'] . \'.php\')'''

s_content = re.sub(r"\\", "\\\\1111", s)


print(s)