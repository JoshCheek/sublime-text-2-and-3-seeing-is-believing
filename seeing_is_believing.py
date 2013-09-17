import sublime, sublime_plugin, subprocess, os

class SeeingIsBelieving(sublime_plugin.TextCommand):
  def run(self, edit):
    # assume one cursor b/c I'm fucking lazy, store its row/col
    (row, col) = self.view.rowcol(self.view.sel()[0].begin())

    # load the text
    region = sublime.Region(0, self.view.size())
    text   = self.view.substr(region)

    # load settings
    settings = sublime.load_settings("Seeing Is Believing.sublime-settings")

    # set up env vars
    env                   = os.environ.copy()
    env_variables         = settings.get("environment_variables")
    environment_variables = ({} if env_variables is None else env_variables) # prob a better way to do this, if you know the pythons, feel free to do it for me :D

    for name, value in environment_variables.items():
      env[name] = value

    # set up the args
    args = []
    ruby_command = os.path.expanduser(settings.get("ruby_command"))
    args.append(ruby_command)
    args.append('-S')
    args.append('seeing_is_believing')
    args.append('--shebang')
    args.append(ruby_command)
    if self.view.file_name() != None:
      args.append("--as")
      args.append(self.view.file_name())

    # subclass defines this
    self.setup_flags(args, settings)

    # call seeing is believing
    s = subprocess.Popen(args, env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = s.communicate(text.encode('utf-8'))
    # display error
    #  error code 1 is displayable errors like exceptions getting raised
    #  non zero/one errors can't be displayed, like syntax error, so we need a dialog box
    if self.should_display_stderr(s.returncode):
      sublime.message_dialog(out[1])
      return

    # replace body with result, reset the selection
    self.view.replace(edit, region, out[0])
    point = self.view.text_point(row, col)
    self.view.sel().clear()
    self.view.sel().add(sublime.Region(point))

class YouKnowThatPlaceBetweenSleepAndAwakeThatPlaceWhereYouStillRememberDreamingThatsWhereIllAlwaysLoveYou(SeeingIsBelieving):
  def setup_flags(self, args, settings):
    for (name, value) in settings.get("flags").items():
      args.append(str(name))
      args.append(str(value))

  def should_display_stderr(self, returncode):
    return returncode != None and returncode != 0 and returncode != 1

class IDrankPoisonForYou(SeeingIsBelieving):
  def setup_flags(self, args, settings):
    args.append('--xmpfilter-style')
    for (name, value) in settings.get("flags").items():
      args.append(str(name))
      args.append(str(value))

  def should_display_stderr(self, returncode):
    return returncode != None and returncode != 0 and returncode != 1

class EveryTimeSomeoneSaysIDoNotBelieveInFairiesSomewhereTheresAFairyThatFallsDownDead(SeeingIsBelieving):
  def setup_flags(self, args, settings):
    args.append('--clean')

  def should_display_stderr(self, returncode):
    return returncode != None and returncode != 0