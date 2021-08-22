# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Brooke")

init python:

    # Mouseover tooltip code from
    # https://lemmasoft.renai.us/forums/viewtopic.php?t=50239

    lexicon = {
        ("d’6", "d'6")  : """You know, the sixth dimension.
        I’m trying to popularize the term…
        really, anything that isn’t “the spirit world” or “the afterlife.”
            """
    }

    def hyperlink_lexicon( str_to_test ):

        for keys in lexicon:

            if isinstance(keys, basestring):
                keys = [keys]

            for phrase in keys:

                # preceded by a space
                str_to_test = str_to_test.replace(
                    " {0}".format(phrase),
                    " {{a=lexicon:{phrase}}}{phrase}{{/a}}".format(
                        phrase = phrase ) )

                # followed by a space
                str_to_test = str_to_test.replace(
                    "{0} ".format(phrase),
                    "{{a=lexicon:{phrase}}}{phrase}{{/a}} ".format(
                        phrase = phrase ) )

        return str_to_test

    config.say_menu_text_filter = hyperlink_lexicon


    def hyperlink_styler(*args):

        return style.hyperlink_text

    def hyperlink_hovered(*args):

        if not args[0]:
            # Ren'Py 7+ recent nightly only, see below
            renpy.hide_screen("lexicon_popup")

        elif args[0][:8] == "lexicon:":

            renpy.show_screen( "lexicon_popup",
                               args[0][8:],
                               renpy.get_mouse_pos() )

            renpy.restart_interaction()

        return

    def hyperlink_clicked(*args):

        if args[0] and args[0][:8] != 'lexicon:':

            # adapted from common/00defaults.rpy
            if args[0].startswith("http:") or args[0].startswith("https:"):
                try:
                    import webbrowser
                    webbrowser.open(args[0])
                except:
                    renpy.notify("Failed to open browser")

            elif args[0].startswith("jump:"):
                renpy.jump( args[0][5:] )

            else:
                renpy.call_in_new_context(args[0][args[0].index(':')+1:])


    style.default.hyperlink_functions = ( hyperlink_styler,
                                          hyperlink_clicked,
                                          hyperlink_hovered )


screen lexicon_popup(phrase=None, pos=(100,100)):

    if phrase:

        python:
            # get description
            d = [ lexicon[k] for k in lexicon if phrase in k ]
            description = d[0] if len(d) else "No description found."
            description = " ".join( [ k for k in description.split()
                                      if k not in [" ", "\t"] ] )

            # move the ypos up by a bit
            pos = ( pos[0], pos[1] - 25 )

            # reformat phrase
            p = [ k for k in lexicon if phrase in k ]
            primary_phrase = p[0][0] if len(p) else phrase
            if primary_phrase != phrase:
                phrase = "{0} ({1})".format(phrase, primary_phrase)

        frame:
            anchor (0.5, 1.0)
            pos pos
            xsize 340
            background Solid("#A9B")
            vbox:
                text "[phrase]" size 18
                text "[description]" size 14

    # Hacky workaround as hyperlink_hovered does not seem to nicely hide this
    # --- Fixed in Ren'Py 7.0 nightlies of May 23rd onwards apparently

    # timer 0.5 action Hide("lexicon_popup")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show brookebasetest

    # These display lines of dialogue.

    b "It’s going to snow tomorrow, or at least it’s very likely."
    b "Either I’m going to be stuck in my room, cycling in heat from d’6 and trying to study,
    or I’m going to be out in the cold helping shovel snow,
    followed by being stuck in my room, only now I’m wet and tired."
    b "So, this is the driving question for tonight:"
    b "What am I going to do…"

menu:

    "Let's go to the campus cafe.":
        jump cafe

    "Let's just get high.":
        jump end_high

label cafe:

    "Placeholder."

label end_high:

    "420"
    # This ends the game.

    return
