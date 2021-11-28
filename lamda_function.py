# -*- coding: utf-8 -*-

"""
Diese Datei enthält verschiedene Klassen und Methoden zur Beantwortung des Alexa-Skills "Ein kleines Weihnachtsrätsel".
Das Sprachmodell von Alexa ist hier nicht enthalten, dieses wird an anderer Stelle im Build auf die verschiedenen "Codewörter" trainiert.
Der Prozess findet dabei automatisiert statt und von außen hat man dort keinen Einblick, hier hat man als Entwickler wenig Spielraum.

Die einzelnen Handler-Klassen in dieser Datei stehen für je eine Funktion, die später unterstützt werden soll. In diesem Fall unterstützt der Skill
bei der Lösung bei von mir gestellten Rätseln mit Hinweissätzen. Für diese Antworten sind je Passwörter zu nennen, die im Sprachmodell
hinterlegt worden sind.
"""

# Import von benötigten Funktionen aus dem Alexa-Sprachmodell und -Kern.
import logging
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

# Wird in dieser Version (noch nicht benötigt)
from utils import create_presigned_url

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

"""
Handler-Klasse für den initialen Start des Skills mit einem Begrüßungssatz.
"""


class LaunchRequestHandler(AbstractRequestHandler):

    # überpprüft, ob diese Klasse die richtige ist, indem die Daten mit dem Sprachmodell abgeglichen werden (siehe Funktion 'Skill-Builder' ganz unten).
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        # Gibt den Typ des Intents (der Anfrage) zurück, die ausgelöst wurde, sofern diese Klasse zutrifft (true). Betrifft nicht den weiteren Verlauf, wird jedoch geloggt.
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    # Diese Funktion generiert eine Antwort basierend auf der Nutzendeneingabe und gibt diese als Response-Builder an die Alexa SSML (Speech Synthesis Markup Language).
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Willkommen! Ich bin hier, um dir bei den Rätseln zu helfen. Nenne mir bitte ein Codewort, dann gebe ich dir den entsprechenden Hinweis."

        # Antwort-Builder bestehend aus einer Antwort und einer identischen Nachfrage, sollten die Nutzenden nicht innerhalb einer festen Zeit antworten.
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


"""
Handler-Klasse für hilfesuchende Nutzende. Gibt Beispiele für Intents, die Nutzende sagen könnten.
"""


class HelpIntentHandler(AbstractRequestHandler):

    # überpprüft, ob diese Klasse die richtige ist, indem die Daten mit dem Sprachmodell abgeglichen werden (siehe Funktion 'Skill-Builder' ganz unten).
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        # Gibt den Typ des Intents (der Anfrage) zurück, die ausgelöst wurde, sofern diese Klasse zutrifft (true). Betrifft nicht den weiteren Verlauf, wird jedoch geloggt.
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    # Diese Funktion generiert eine Antwort basierend auf der Nutzendeneingabe und gibt diese als Response-Builder an die Alexa SSML (Speech Synthesis Markup Language).
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Du kannst mir verschiedene Codewörter sagen und falls dieses korrekt ist, gebe ich dir eine entsprechende Antwort."

        # Antwort-Builder bestehend aus einer Antwort und einer identischen Nachfrage, sollten die Nutzenden nicht innerhalb einer festen Zeit antworten.
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


"""
Handler-Klasse für Pause-, Abbruch- oder Stop-Intents, die den Skill unterbrechen oder beenden sollen.
"""


class CancelOrStopIntentHandler(AbstractRequestHandler):

    # überpprüft, ob diese Klasse die richtige ist, indem die Daten mit dem Sprachmodell abgeglichen werden (siehe Funktion 'Skill-Builder' ganz unten).
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        # Gibt den Typ des Intents (der Anfrage) zurück, die ausgelöst wurde, sofern diese Klasse zutrifft (true). Betrifft nicht den weiteren Verlauf, wird jedoch geloggt.
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    # Diese Funktion generiert eine Antwort basierend auf der Nutzendeneingabe und gibt diese als Response-Builder an die Alexa SSML (Speech Synthesis Markup Language).
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Bis zum nächsten Mal!"

        # Antwort-Builder bestehend aus einer Antwort.
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


"""
Handler-Klasse für Fallback-Intents, wenn ein Codewort nicht richtig verstanden worden ist. Ein Großteil der Fehler wird hier bereits abgefangen.
"""


class FallbackIntentHandler(AbstractRequestHandler):

    # überpprüft, ob diese Klasse die richtige ist, indem die Daten mit dem Sprachmodell abgeglichen werden (siehe Funktion 'Skill-Builder' ganz unten).
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        # Gibt den Typ des Intents (der Anfrage) zurück, die ausgelöst wurde, sofern diese Klasse zutrifft (true). Betrifft nicht den weiteren Verlauf, wird jedoch geloggt.
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    # Diese Funktion generiert eine Antwort basierend auf der Nutzendeneingabe und gibt diese als Response-Builder an die Alexa SSML (Speech Synthesis Markup Language).
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Tut mir Leid, entweder gibt es diesen Code nicht oder ich habe ihn nicht korrekt verstanden."
        reprompt = "Das habe ich nicht verstanden. Kannst du das noch einmal wiederholen?"

        # Antwort-Builder bestehend aus einer Antwort und einer identischen Nachfrage, sollten die Nutzenden nicht innerhalb einer festen Zeit antworten (hier als Einzeiler).
        return handler_input.response_builder.speak(speech).ask(reprompt).response


"""
Handler-Klasse für das Beenden einer Session. Eine Antwort wird hier nicht gegeben, diese wird bereits mittels des Stop-Intenthandlers gegeben.
"""


class SessionEndedRequestHandler(AbstractRequestHandler):

    # überpprüft, ob diese Klasse die richtige ist, indem die Daten mit dem Sprachmodell abgeglichen werden (siehe Funktion 'Skill-Builder' ganz unten).
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        # Gibt den Typ des Intents (der Anfrage) zurück, die ausgelöst wurde, sofern diese Klasse zutrifft (true). Betrifft nicht den weiteren Verlauf, wird jedoch geloggt.
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    # Diese Funktion generiert eine Antwort basierend auf der Nutzendeneingabe und gibt diese als Response-Builder an die Alexa SSML (Speech Synthesis Markup Language).
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Antwort-Builder bestehend aus einer Antwort und einer identischen Nachfrage, sollten die Nutzenden nicht innerhalb einer festen Zeit antworten.
        return handler_input.response_builder.response


"""
Handler-Klasse für das Testen von Methoden. Wird nur während der Entwicklung eingesetzt um zu überprüfen, ob Intents richtig getriggert werden.
In der finalen Version ist diese Klasse deswegen auskommentiert und kommt auch im Skill-Builder nicht vor.
"""
"""class IntentReflectorHandler(AbstractRequestHandler):
    The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.

    # überpprüft, ob diese Klasse die richtige ist, indem die Daten mit dem Sprachmodell abgeglichen werden (siehe Funktion 'Skill-Builder' ganz unten).
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        # Gibt den Typ des Intents (der Anfrage) zurück, die ausgelöst wurde, sofern diese Klasse zutrifft (true). Betrifft nicht den weiteren Verlauf, wird jedoch geloggt.
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    # Diese Funktion generiert eine Antwort basierend auf der Nutzendeneingabe und gibt diese als Response-Builder an die Alexa SSML (Speech Synthesis Markup Language).
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "Du hast gerade " + intent_name + " ausgelöst."

        # Antwort-Builder bestehend aus einer Antwort und einer identischen Nachfrage, sollten die Nutzenden nicht innerhalb einer festen Zeit antworten.
        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )"""

"""
Handler-Klasse für Fehlermeldungen, die nicht durch die Fallback-Klasse abgefangen werden.
Also: Fehler im Quellcode, fatale Fehler, Verbindungsabbrüche etc.
"""


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """

    # überpprüft, ob diese Klasse die richtige ist, indem die Daten mit dem Sprachmodell abgeglichen werden (siehe Funktion 'Skill-Builder' ganz unten).
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool

        # Gibt den Typ des Intents (der Anfrage) zurück, die ausgelöst wurde, sofern diese Klasse zutrifft (true). Betrifft nicht den weiteren Verlauf, wird jedoch geloggt.
        # Sollte ein Fehler auftreten, wird automatisch diese Klasse aufgerufen und die Nutzenden werden gebeten, die Eingabe zu wiederholen.
        return True

    # Diese Funktion generiert eine Antwort basierend auf der Nutzendeneingabe und gibt diese als Response-Builder an die Alexa SSML (Speech Synthesis Markup Language).
    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Tut mir Leid, entweder gibt es diesen Code nicht oder ich habe ihn nicht korrekt verstanden."

        # Antwort-Builder bestehend aus einer Antwort und einer identischen Nachfrage, sollten die Nutzenden nicht innerhalb einer festen Zeit antworten.
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


"""
Handler-Klasse für den ersten Hinweis, der im Laufe des Spiels erlangt wird.
"""


class HintOneIntentHandler(AbstractRequestHandler):

    # überpprüft, ob diese Klasse die richtige ist, indem die Daten mit dem Sprachmodell abgeglichen werden (siehe Funktion 'Skill-Builder' ganz unten).
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        # Gibt den Typ des Intents (der Anfrage) zurück, die ausgelöst wurde, sofern diese Klasse zutrifft (true). Betrifft nicht den weiteren Verlauf, wird jedoch geloggt.
        return ask_utils.is_intent_name("HintOneIntent")(handler_input)

    # Diese Funktion generiert eine Antwort basierend auf der Nutzendeneingabe und gibt diese als Response-Builder an die Alexa SSML (Speech Synthesis Markup Language).
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Du solltest mal ganz genau dein Buch 'Robinson Crusoe' unter die Lupe nehmen, eventuell versteckt sich hier die Lösung."

        # Antwort-Builder bestehend aus einer Antwort.
        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


"""
Handler-Klasse für den zweiten Hinweis, der im Laufe des Spiels erlangt wird.
"""


class HintTwoIntentHandler(AbstractRequestHandler):

    # überpprüft, ob diese Klasse die richtige ist, indem die Daten mit dem Sprachmodell abgeglichen werden (siehe Funktion 'Skill-Builder' ganz unten).
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        # Gibt den Typ des Intents (der Anfrage) zurück, die ausgelöst wurde, sofern diese Klasse zutrifft (true). Betrifft nicht den weiteren Verlauf, wird jedoch geloggt.
        return ask_utils.is_intent_name("HintTwoIntent")(handler_input)

    # Diese Funktion generiert eine Antwort basierend auf der Nutzendeneingabe und gibt diese als Response-Builder an die Alexa SSML (Speech Synthesis Markup Language).
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Oh kommt, all ihr Hoffnungsvollen, und singt mir ein Lied. Die Noten Drei und Sechzehn geben die Buchstaben vor und der Takt das zugehörige Wort."

        # Antwort-Builder bestehend aus einer Antwort.
        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


"""
Handler-Klasse für den ersten (jedoch in jeddem Fall falschen) Versuch, das Rätsel am Ende zu lösen mit der Mitteilung, den letzten Hinweis noch abzuwarten.
"""


class PuzzleSolveFalseIntentHandler(AbstractRequestHandler):

    # überpprüft, ob diese Klasse die richtige ist, indem die Daten mit dem Sprachmodell abgeglichen werden (siehe Funktion 'Skill-Builder' ganz unten).
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        # Gibt den Typ des Intents (der Anfrage) zurück, die ausgelöst wurde, sofern diese Klasse zutrifft (true). Betrifft nicht den weiteren Verlauf, wird jedoch geloggt.
        return ask_utils.is_intent_name("PuzzleSolveFalseIntent")(handler_input)

    # Diese Funktion generiert eine Antwort basierend auf der Nutzendeneingabe und gibt diese als Response-Builder an die Alexa SSML (Speech Synthesis Markup Language).
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Leider war das nicht die richtige Lösung, du solltest den letzten Hinweis noch abwarten, vielleicht ergibt sich dann die Lösung."

        # Antwort-Builder bestehend aus einer Antwort.
        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


"""
Handler-Klasse für zweiten Versuch, das Weihnachtsrätsel zu lösen, der mit einer richtigen Lösung und einem QR-Code belohnt wird.
"""


class SecondPuzzleSolveIntentHandler(AbstractRequestHandler):

    # überpprüft, ob diese Klasse die richtige ist, indem die Daten mit dem Sprachmodell abgeglichen werden (siehe Funktion 'Skill-Builder' ganz unten).
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        # Gibt den Typ des Intents (der Anfrage) zurück, die ausgelöst wurde, sofern diese Klasse zutrifft (true). Betrifft nicht den weiteren Verlauf, wird jedoch geloggt.
        return ask_utils.is_intent_name("SecondPuzzleSolveIntent")(handler_input)

    # Diese Funktion generiert eine Antwort basierend auf der Nutzendeneingabe und gibt diese als Response-Builder an die Alexa SSML (Speech Synthesis Markup Language).
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Herzlichen Glückwunsch, du hast alle Rätsel gelöst! Der Game Master und ich wünschen dir eine frohe Weihnachten, genieße die Zeit mit deiner Familie! PS: Schau genau in deiner Handtasche nach einem QR-Code für eine kleine Überraschung!"

        # Antwort-Builder bestehend aus einer Antwort.
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


"""class PuzzleSolveIntentHandler(AbstractRequestHandler):

    # überpprüft, ob diese Klasse die richtige ist, indem die Daten mit dem Sprachmodell abgeglichen werden (siehe Funktion 'Skill-Builder' ganz unten).
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        # Gibt den Typ des Intents (der Anfrage) zurück, die ausgelöst wurde, sofern diese Klasse zutrifft (true). Betrifft nicht den weiteren Verlauf, wird jedoch geloggt.
        return ask_utils.is_intent_name("PuzzleSolveIntent")(handler_input)

    # Diese Funktion generiert eine Antwort basierend auf der Nutzendeneingabe und gibt diese als Response-Builder an die Alexa SSML (Speech Synthesis Markup Language).
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Herzlichen Glückwunsch, du hast alle Rätsel gelöst! Mit diesem Song, gespielt auf der Okarina, wünsche ich dir nun eine frohe Weihnachten, genieße die Zeit mit deiner Familie!"

        # Antwort-Builder bestehend aus einer Antwort und einem Song, der von einer URL abgerufen wird.
        return (
            handler_input.response_builder
                .speak(speak_output)
                #.play(song, "token")
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )"""

# Das SkillBuilder-Objekt leitet alle Anfragen und Antworten zu den Handlern, wo diese weiterverarbeitet werden.
# Hier sollten alle oben definierten Handler aufgeführt sein, da sie sonst nicht angepsrochen werden können.
# Die Reihenfolge zählt dabei: Anfragen werden von oben nach unten durch die Handler geschickt. Wird also einer ausgelöst,
# wird er nicht an die Handler darunter weitergeleitet. Wichtig ist, dass der Exception-Handler ganz am Ende steht,
# da dieser egal bei welcher Anfrage auslöst und quasi als Auffangnetz fungiert.
sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(HintOneIntentHandler())
sb.add_request_handler(HintTwoIntentHandler())
sb.add_request_handler(PuzzleSolveFalseIntentHandler())
sb.add_request_handler(SecondPuzzleSolveIntentHandler())
# sb.add_request_handler(PuzzleSolveIntentHandler())
# sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()