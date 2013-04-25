import sublime, sublime_plugin, subprocess, os

class YouKnowThatPlaceBetweenSleepAndAwakeThatPlaceWhereYouStillRememberDreamingThatsWhereIllAlwaysLoveYou(sublime_plugin.TextCommand):
  def run(self, edit):
    region = sublime.Region(0, self.view.size())
    text   = self.view.substr(region)
    env    = os.environ.copy()
    env['RBENV_VERSION'] = '2.0.0-p0'
    s      = subprocess.Popen(
      ['/Users/joshcheek/.rbenv/shims/ruby', '-S', 'seeing_is_believing',
          '-Ku',
          '--result-length', '500',
      ],
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
