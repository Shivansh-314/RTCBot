from botbuilder.core import TurnContext
from botbuilder.core import CardFactory
from botbuilder.core import MessageFactory
from botbuilder.schema import CardAction
from botbuilder.schema import ActionTypes
import botbuilder.schema

class EchoBot:

    async def on_turn(self,turn_context:TurnContext):
        sendMessage = "default"

        recievedMessage = turn_context.activity.text
        recievedMessage = recievedMessage.strip()
        recievedMessage = recievedMessage.lower()

        messageContents = recievedMessage.split()

        if(messageContents[0] == "wi"):
            if(messageContents[1].isnumeric()):
                workItemNumber = int(messageContents[1])
                sendMessage = "Work Item Title " + messageContents[1]
            else:
                sendMessage = "Invalid Work Item Number"

        #sendMessage = recievedMessage

        #await turn_context.send_activity(sendMessage)
        
        card = CardFactory.hero_card(botbuilder.schema._models_py3.HeroCard(
        title="Welcome to RTC Bot",
        text="This bot connects to RTC to get the workitems' information",
        buttons=[
            CardAction(
                type=ActionTypes.im_back, title="1. Inline Attachment", value="1"
            ),
            CardAction(
                type=ActionTypes.im_back, title="2. Internet Attachment", value="2"
            ),
            CardAction(
                type=ActionTypes.im_back, title="3. Uploaded Attachment", value="3"
            ),
        ],));

        message = MessageFactory.attachment(card);
        await turn_context.send_activity(message);