# format
import sublime_plugin
import sublime


class AutoSemiColonCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        last_pos = []
        smart_insert = True
        for sel in view.sel():
            if not sel.empty():
                smart_insert = False
                break

            last = last_bracket = first = sel.end()
            while (view.substr(last) in [' ', ')', ']', '}']):
                if (view.substr(last) != ' '):
                    last_bracket = last + 1
                last += 1

            if (last_bracket < last):
                last = last_bracket

            if last > first:
                last_pos.append(last)
            else:
                smart_insert = False
                break

        if smart_insert:
            view.sel().clear()
            for last in last_pos:
                view.sel().add(sublime.Region(last, last))
            view.run_command("insert", {"characters": ";\n"})
        else:
            view.run_command("insert", {"characters": ";"})
