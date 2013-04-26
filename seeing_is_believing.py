import sublime, sublime_plugin, subprocess, os

class YouKnowThatPlaceBetweenSleepAndAwakeThatPlaceWhereYouStillRememberDreamingThatsWhereIllAlwaysLoveYou(sublime_plugin.TextCommand):
  def run(self, edit):
    # load the text
    region = sublime.Region(0, self.view.size())
    text   = self.view.substr(region)

    # load settings
    settings = sublime.load_settings("Seeing Is Believing.sublime-settings")

    # set up env vars
    env = os.environ.copy()
    for (name, value) in settings.get("environment_variables").iteritems():
      env[name] = value

    # set up the args
    args = []
    args.append(os.path.expanduser(settings.get("ruby_command")))
    args.append('-S')
    args.append('seeing_is_believing')
    for (name, value) in settings.get("flags").iteritems():
      args.append(str(name))
      args.append(str(value))
    if self.view.file_name() != None:
      args.append("--as")
      args.append(self.view.file_name())

    # call seeing is believing
    s = subprocess.Popen(args, env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = s.communicate(text.encode('utf-8'))

    # display error
    #  error code 1 is displayable errors like exceptions getting raised
    #  non zero/one errors can't be displayed, like syntax error, so we need a dialog box
    if s.returncode != None and s.returncode != 0 and s.returncode != 1:
      sublime.message_dialog(out[1])
      return

    # replace body with result
    self.view.replace(edit, region, out[0])

class EveryTimeSomeoneSaysIDoNotBelieveInFairiesSomewhereTheresAFairyThatFallsDownDead(sublime_plugin.TextCommand):
  def run(self, edit):
    region = sublime.Region(0, self.view.size())
    text   = self.view.substr(region)
    env    = os.environ.copy()
    env['RBENV_VERSION'] = '2.0.0-p0'
    s      = subprocess.Popen(
      ['/Users/joshcheek/.rbenv/shims/ruby', '-S', 'seeing_is_believing', '--clean'],
      env=env,
      stdin=subprocess.PIPE,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE
    )
    out = s.communicate(text.encode('utf-8'))
    if s.returncode != None and s.returncode != 0:
      sublime.message_dialog(out[1])
      return

    self.view.replace(edit, region, out[0])
