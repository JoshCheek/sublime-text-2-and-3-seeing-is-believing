import sublime, sublime_plugin, subprocess

class ExecuteAndUpdateRubyMarkersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = sublime.Region(0, self.view.size())
        text = self.view.substr(region)

        s = subprocess.Popen(
            [ '/usr/bin/env', 'xmpfilter' ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE )
        out = s.communicate(text.encode('utf-8'))
        if s.returncode != None and s.returncode != 0:
            sublime.message_dialog("There was an error: " + out[1])
            return

        self.view.replace(edit, region, out[0])

class SetRubyMarkersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = sublime.Region(0, self.view.size())
        text = self.view.substr(region)

        s = subprocess.Popen(
            [ '/usr/bin/env', 'xmpfilter', '-m' ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE )
        out = s.communicate(text.encode('utf-8'))
        if s.returncode != None and s.returncode != 0:
            sublime.message_dialog("There was an error: " + out[1])
            return

        self.view.replace(edit, region, out[0])
