def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session):
    return welcomeuser()

def onIntent(intentRequest, session):
             
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']
    if intentName == "rubiksIntent":
        return fun_math(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def welcomeuser():
    sessionAttributes = {}
    cardTitle = " Hello"
    speechOutput =  "Hello , Welcome to rubiks learn! " \
                    "You can know interesting facts about rubiks cubes by saying rubiks fun"
    repromptText =  "You can know interesting facts about rubiks cubes by saying rubiks fun"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def fun_math(intent, session):
    import random
    index = random.randint(0,len(prime)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "Did you know that, " + prime[index] 
    repromptText = "You can know interesting facts about rubiks cubes by saying rubiks fun"
    shouldEndSession = False                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using rubiks learn Alexa Skills Kit. " \
                    "Have a great time! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
            },
            
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }


def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }



prime = [ "The first Magic Cube, as it was originally known, was sold in a Budapest toy shop in 1975",
          "The Magic Cube was renamed Rubik's Cube in 1980",
          "With six coloured sides, 21 pieces and 54 outer surfaces, there's a combined total of over 43 quintillioin different possible configurations",
          "The world record for solving a 3 by 3 rubiks cube is 4.59 seconds",
          "Some people can even solve it blindfolded",
          "rubiks cube was invented by erno rubik in 1974",
          "solving a rubiks cube again and again can help you improve your hand-eye coordination and your memory",
          "Any 3 by 3 rubik cube can be solved in under 20 moves, otherwise known as the God's Number",
          "Any legal configuration of a rubiks can only be obtained by an even number of swaps of pieces."
        ]
