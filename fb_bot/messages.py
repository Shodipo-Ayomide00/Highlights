import emoji


# EMOJIS

def emo(alias):
    return emoji.emojize(alias, use_aliases=True)


EMOJI_WAVE = emo(':wave:')
EMOJI_MAGNIFYING_GLASS = emo(':mag:')
EMOJI_NOTIFICATION = emo(':bell:')
EMOJI_CROSS = emo(':x:')
EMOJI_ADD = emo(':heavy_plus_sign:')
EMOJI_REMOVE = emo(':heavy_minus_sign:')
EMOJI_DONE = emo(':ok_hand:')
EMOJI_HELP = emo(':question:')
EMOJI_FOOTBALL = emo(':soccer:')
EMOJI_ONE = '1)'
EMOJI_TWO = '2)'
EMOJI_SWEAT = emo(':cold_sweat:')
EMOJI_INNONCENT = emo(':innocent:')
EMOJI_BROKEN_HEART = emo(':broken_heart:')
EMOJI_THUMBS_UP = emo(':+1:')
EMOJI_FIRE = emo(':fire:')
EMOJI_TV = emo(':tv:')
EMOJI_MUSCLE = emo(':muscle:')
EMOJI_CLAP = emo(':clap:')
EMOJI_EXPLOSION = emo(':boom:')


# MESSAGES

HELP_MESSAGE = "Here is what you can ask me:\n\n" \
               + EMOJI_ONE + " Press \"Search highlights\" and I will give you the latest highlights videos for a team\n\n" \
               + EMOJI_TWO + " Press \"My teams\" to subscribe to teams and I will send you highlights videos as soon as the match is over!"

WHAT_DO_YOU_WANT_TODO_MESSAGE = "What can I do for you? " + EMOJI_INNONCENT

ANYTHING_ELSE_I_CAN_DO_MESSAGE = "Anything else I can do for you? " + EMOJI_INNONCENT

CANCEL_MESSAGE = "Alright let's stop there then :)"

DONE_MESSAGE = "You're good to go!\n I will send you the latest highlights for your teams as soon as the videos are available. " + EMOJI_TV

SEARCH_HIGHLIGHTS_MESSAGE = "Tell me for which team should I give you highlight videos? " + EMOJI_TV

NO_HIGHLIGHTS_MESSAGE = "I'm so sorry but I could not find any recent highlight video for your team " + EMOJI_BROKEN_HEART + " They must have not play for a long time."

GET_STARTED_MESSAGE = "Hey {}, " + EMOJI_WAVE + "\n\nI am the smart bot that fetches the latest football highlights for you."

GET_STARTED_MESSAGE_2 = "I will guide you throughout this tutorial. To get started, enter the name of any " + EMOJI_FOOTBALL + " team you would love to subscribe to."

NOTIFICATION_MESSAGE = "I am currently sending you the highlights for the following " + EMOJI_FOOTBALL + " teams: \n\n{}\n\nDo you want to ADD or REMOVE a team?"

ADD_TEAM_MESSAGE = "Tell me the name of the team you want to add " + EMOJI_FIRE

DELETE_TEAM_NOT_FOUND_MESSAGE = "I did not find this team to remove :/ Please choose one of the followings"

DELETE_TEAM_MESSAGE = "Which team do you want to remove?"

TEAM_RECOMMEND_MESSAGE = "I did not find your team " + EMOJI_BROKEN_HEART +" Did you mean?"

TEAM_NOT_FOUND_MESSAGE = "I did not find your team " + EMOJI_BROKEN_HEART + " Try entering the full name of the team."

TEAM_ADDED_SUCCESS_MESSAGE = "{} was successfully added to your teams " + EMOJI_THUMBS_UP

TEAM_ADDED_FAIL_MESSAGE = "I could not find the team: {}"

TEAM_DELETED_MESSAGE = "{} successfully removed from your teams " + EMOJI_THUMBS_UP

NO_MATCH_FOUND_TEAM_RECOMMENDATION = "I did not find highlights for your team " + EMOJI_BROKEN_HEART + " Did you mean?"

NO_MATCH_FOUND = "I did not find highlights for your team! " + EMOJI_BROKEN_HEART

ERROR_MESSAGE = "I am sorry, but an error occured " + EMOJI_SWEAT

NEW_HIGHLIGHT_MESSAGE = "Hey {} " + EMOJI_WAVE + " Here is a new highlight video for your " + EMOJI_FOOTBALL + " team {}."

TUTORIAL_MESSAGE = "Awesome " + EMOJI_CLAP * 2 + " I will now send you the latest highlight videos for {} at the end of every match in the following format. Clicking on the message will redirect you to the video " + EMOJI_TV

THANK_YOU = "Don't say thanks! That's my job " + EMOJI_MUSCLE