import sublime
import sublime_plugin

class SetGlobalFontSizeCommand(sublime_plugin.ApplicationCommand):
  def is_checked(self, new_size):
    s = sublime.load_settings("Preferences.sublime-settings")
    return s.get("font_size") == new_size

  def run(self, new_size):
    s = sublime.load_settings("Preferences.sublime-settings")
    s.set("font_size", new_size)
    sublime.save_settings("Preferences.sublime-settings")
