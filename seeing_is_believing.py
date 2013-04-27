import sublime, sublime_plugin, subprocess, os

class SeeingIsBelieving(sublime_plugin.TextCommand):
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

    # replace body with result
    self.view.replace(edit, region, out[0])


class YouKnowThatPlaceBetweenSleepAndAwakeThatPlaceWhereYouStillRememberDreamingThatsWhereIllAlwaysLoveYou(SeeingIsBelieving):
  def setup_flags(self, args, settings):
    for (name, value) in settings.get("flags").iteritems():
      args.append(str(name))
      args.append(str(value))
    if self.view.file_name() != None:
      args.append("--as")
      args.append(self.view.file_name())

  def should_display_stderr(self, returncode):
    return returncode != None and returncode != 0 and returncode != 1

class EveryTimeSomeoneSaysIDoNotBelieveInFairiesSomewhereTheresAFairyThatFallsDownDead(SeeingIsBelieving):
  def setup_flags(self, args, settings):
    args.append('--clean')
    if self.view.file_name() != None:
      args.append("--as")
      args.append(self.view.file_name())

  def should_display_stderr(self, returncode):
    return returncode != None and returncode != 0
