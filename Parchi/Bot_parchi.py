from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
#import sqlite3
#from math import radians, cos, sin, asin, sqrt


with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Il tuo token è ", TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Benvenuti nel servizio di ricerca parchi Verona\nPer scegliere la località digitare /localita")

async def localita(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Scegli tra queste località:\n/Valeggio\n/Sommacampagna\n/Sona\n/Palazzolo_di_sona\n/Lugagnano_di_sona\n/San_giorgio_in_salici\n/Pescantina\n/Mozzecane\n/Pastrengo\n/Villafranca\n/Castelnuovo")
    

async def Valeggio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    x= "PARCO ICHENHAUSEN	VIA ROBERT BADEN-POWELL, VALEGGIO SUL MINCIO\n\nFANTE	VIA DEL FANTE, VALEGGIO SUL MINCIO\nCOMBONI	VIA SAN DANIELE COMBONI, VALEGGIO SUL MINCIO\n\nFASCINELLI	VIA ADELINO FASCINELLI, VALEGGIO SUL MINCIO\n\nDELLA RIMEMBRANZA	PIAZZALE VITTORIO VENETO, VALEGGIO SUL MINCIO\n\nVERDE PALAZZETTO	VIA DELLO SPORT\n\nBELLUNO	VICOLO BELLUNO, VALEGGIO SUL MINCIO\n\nBRENTA	VIA BRENTA, VALEGGIO SUL MINCIO\n\nTAGLIAMENTO	VIA TAGLIAMENTO, VALEGGIO SUL MINCIO\n\nMAZZINI	VIA GIUSEPPE MAZZINI, VALEGGIO SUL MINCIO\n\nRICCI	VIA MATTEO RICCI, VALEGGIO SUL MINCIO\n\nPOETI	VIA DEI POETI. VALEGGIO SUL MINCIO\n\nTRIESTE	VIA TRIESTE, VALEGGIO SUL MINCIO\n\nPONTIERI	VIA DEI PONTIERI, VALEGGIO SUL MINCIO\n\nFALCONE	VIA GIOVANNI FALCONE, VALEGGIO SUL MINCIO\n\nFINCATO	VIA COLONNELLO GIOVANNI FINCATO, VALEGGIO SUL MINCIO\n\nFALLACI	VIA ORIANA FALLACI, VALEGGIO SUL MINCIO\n\nFANTE	VIA DEL FANTE, VALEGGIO SUL MINCIO\n\nPARTIGIANI	VIA DEI PARTIGIANI, VALEGGIO SUL MINCIO\n\nBERSAGLIERE	VIA DEL BERSAGLIERE, VALEGGIO SUL MINCIO\n\nSAN PIETRO	VIA SAN PIETRO, VALEGGIO SUL MINCIO\n\nVERONA	VIA VERONA, VALEGGIO SUL MINCIO\n\nVENEZIA	VIA VENEZIA, VALEGGIO SUL MINCIO\n\nISONZO	VIA ISONZO, VALEGGIO SUL MINCIO\n\nICHENHAUSEN	VIA ROBERT BADEN-POWELL, VALEGGIO SUL MINCIO\n\nICHENHAUSEN	VIA ROBERT BADEN-POWELL, VALEGGIO SUL MINCIO\n\nFINCATO	VIA COLONNELLO GIOVANNI FINCATO, VALEGGIO SUL MINCIO\n\nICHENHAUSEN	VIA GORIZIA, VALEGGIO SUL MINCIO\n\nSCUOLA DELLINFANZIA IL MELOGRANO VIA DEGLI ALPINI, VALEGGIO SUL MINCIO\n\nICHENHAUSEN	VIALE PAPA GIOVANNI VENTITREESIMO, VALEGGIO SUL MINCIO\n\nICHENHAUSEN	VIA ROBERT BADEN-POWELL, VALEGGIO SUL MINCIO\n\nPO	VICOLO PO, VALEGGIO SUL MINCIO\n\nMORO	VIA ALDO MORO, VALEGGIO SUL MINCIO\n\nMATTEOTTI	VIA GIACOMO MATTEOTTI, VALEGGIO SUL MINCIO\n\nBORSELLINO	VIA PAOLO BORSELLINO, VALEGGIO SUL MINCIO\n\nFASCINELLI	VIA ADELINO FASCINELLI, VALEGGIO SUL MINCIO\n\nFANTE	VIA DEL FANTE, VALEGGIO SUL MINCIO\n\nFANTE	VIA DEL FANTE, VALEGGIO SUL MINCIO\n\nSCUOLA PRIMARIA  CARLO COLLODI 	PIAZZA GIUSEPPE GARIBALDI, VALEGGIO SUL MINCIO\n\nGIARDINI DI BORGHETTO	VIA PONTE VISCONTEO\n\nPUNTA BORGHETTO	VIA MICHELANGELO BUONARROTI, BORGHETTO\n\nSANZIO	VIA RAFFAELLO SANZIO, BORGHETTO\n\nSCUOLA DELL INFANZIA  CA  PRATO 	LOCALITA  FONTANELLO\n\nMONTE COCOLO	VICOLO MONTE COCOLO, LOCALITA SANTA LUCIA AI MONTI\n\nNIKOLAJEWKA	PIAZZA NIKOLAJEWKA, SALIONZE\n\nTEODORICO	VICOLO TEODORICO, SALIONZE\n\nATTILA	VIA ATTILA, SALIONZE\n\nUNNI	VIA DEGLI UNNI, SALIONZE\n\nALPI	VIA DELLE ALPI, SALIONZE\n\nBENACO	VIA BENACO, SALIONZE\n\nPASTRENGO	VIA PASTRENGO, SALIONZE\n\nTEODORICO	VICOLO TEODORICO, SALIONZE\n\nPACINOTTI	VIA ANTONIO PACINOTTI, VALEGGIO SUL MINCIO\n\nARMONIA	VIA DELLARMONIA, LOCALITA FORONI\n\nCONCORDIA	VIA DELLA CONCORDIA, LOCALITA' FORONI\n\nFERMI	VIA ENRICO FERMI, LOCALITA FORONI\n\nIMPRENDITORI	IMPRENDITORI, VALEGGIO SUL MINCIO\n\nPIGOZZI	VIA DON LEONE PIGOZZI, LOCALITA VANONI-REMELLI\n\nPIGOZZI	VIA DON LEONE PIGOZZI, LOCALITA VANONI-REMELLI\n\nASILO NIDO GLI GNOMI	LOCALITA VANONI-REMELLI"
    await update.message.reply_text(x.lower())

async def Sommacampagna(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Parco pubblico Villa Venier\nParco Baleno\nParco della Bissara\nParco Caprioli\nParco Giochi Monte Molin\nGiardini di Piazza della Repubblica\nParco pubblico")

async def Sona(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Parco via Don Vittorio Castello	Via Don Vittorio Castello, San Giorgio in Salici\n\nParco via Segradi	Via Segradi, angolo via Palladio, San Giorgio in Salici\n\nParco giochi Baita Alpini	Via Tiziano, San Girgio in Salici")

async def Palazzolo_di_sona(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Parco giochi Via Prele	Via Prele, Palazzolo di Sona\nParco Via Salgari	Via Salgari, Palazzolo di Sona\nParco via Castello, Torre Scaligera	Via Castello, Palazzolo di Sona\nParco via Gonella	Via Gonella, Palazzolo di Sona\n")

async def Lugagnano_di_sona(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("""Parco giochi via Cattaneo	Via Cattaneo, Mancalacqua, Sona (VR)\n
Parco del foglio	Via Carducci, Lugagnano di Sona (VR)\n
Parco giochi Via C.A. Dalla Chiesa	Via Generale C A Dalla Chiesa\n
Area Cani, via Fermi	Via Fermi, Lugagnano di Sona\n
Parco Giochi, via Marco Polo	Via Marco Polo, Lugagnano di Sona\n
Parco giochi Via Tirso/via Reno	Via Tirso, Lugagnano di Sona (VR)\n
Parco giochi Via Ticino	Via Ticino, Lugagnano di Sona\n
Parco Tortella	Via Volturno, Lugagnano di Sona\n
Parco Franco Conti	Via Colombo, Lugagnano di Sona\n""")

async def San_giorgio_in_salici(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("""Parco via Don Vittorio Castello	Via Don Vittorio Castello, San Giorgio in Salici\n
Parco via Segradi	Via Segradi, angolo via Palladio, San Giorgio in Salici\n
Parco giochi Baita Alpini	Via Tiziano, San Girgio in Salici\n""")

async def Pescantina(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("""Giardino	via M. Pastello\n
parco giochi ed aiuola	via Busa\n
Parco via Don Morandin	via Don Morandin\n
Parco via Almirante	via Almirante\n
parco giochi via Don Calabria	via Don Calabria\n
Area via S. Francesco	via S. Francesco\n
Piazza Tanti Balconi	Piazza Tanti Balconi\n
Via Postale vecchia  Campetto	Via Postale vecchia\n
Via Siedlce -Via S. Francesco 3 aree	Via Siedlce -Via S. Francesco\n
Parco via dei Peschi	via dei Peschi\n
area cinofila	Via dei Pini\n
parco giochi via Bertoldi	via Bertoldi\n
area via Verdi via Rossini	via Verdi via Rossini\n
parco giochi via Vicentini	via Vicentini\n
via Vivaldi	via Vivaldi\n
parco giochi Corte regia	Corte regia\n
parco Padre Zeno	via Belvedere\n
Parco giochi via M. Castagna	via M. Castagna\n
Parco via Zenati	via Zenati\n
Via Don Ottoboni	Via Don Ottoboni\n
Area Donatori Sangue	via Moletti\n
Area via dei sassi	via dei sassi\n
Area verde lottizzazione Sabionè	via Salvo D'Acquisto\n
Area via Anita Garibaldi	via Anita Garibaldi\n
Area via caduti del lavoro	via caduti del lavoro\n
Giardino Via Vegra	Via Vegra\n
Parco giochi via Vezza	via Vezza\n
Area Verde Via Papa paolo VI	Via Papa paolo VI\n
Area Verde via Bogoni-via Zamboni	via Zamboni\n
via Beghini	via Beghini\n
Lottizzazione Serena 3 aree verdi	via Girelli/via Pascoli\n
Area Verde via Papa Giovanni 23°	via Papa Giovanni 23°\n
area verde viale Verona incrocio via Lora	viale Verona incrocio via Lora\n
Parco giochi Via Falcone	Via Falcone\n
Area verde via Martiri della Libertà	via Martiri della Libertà\n
Parco giochi via Butturini	via Butturini\n
Area Verde via Butturini	via Butturini\n""")

async def Mozzecane(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("Via San Valentino\nVia Giuseppe Mazzini\nVia Don Giuseppe Bonizzato\nVia Vittorio Bachelet\nVia Caduti di Nassirya\nVia Quistello\nVia San Lorenzo\nVia Salvo d'Acquisto\nTraversa di Via Ponte\nVia Crocetta\nVia Sant Antonio Abate\nVia Francesco Miniscalchi\nVia Gino Ferroni\nVia Anna Frank\nVia Francesco Miniscalchi\nVia del Bersagliere\nVia Berto Barbarani\nVia Giuseppe Verdi\nVia Don Germano Alberti\Via Dante Alighieri\nVia Ugo Foscolo\nVia Giacomo Leopardi\nVia Gino Ferroni\nVia San Faustino\nVia XXV Aprile\nVia Giovanni Falcone")
   
async def Pastrengo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("""Via dell'Aviere	Via dell'Aviere - 37010 Pastrengo (VR)\n
Via del Fante	Via del Fante - 37010 Pastrengo (VR)\n
Via dei Capitelli	Via dei Capitelli - 37010 Pastrengo (VR)\n
Via Papa Luciani	Via Papa Luciani - 37010 Pastrengo (VR)\n
Via Maggiore Alessandro Negri di Sanfront	Via Maggiore Alessandro Negri di Sanfront - 37010 Pastrengo (VR)\n
Via Primo Maggio	Via Primo Maggio - 37010 Pastrengo (VR)\n
Via del Bersagliere	Via del Bersagliere - 37010 Pastrengo (VR)\n
Piazza del Donatore	Piazza del Donatore - 37010 Pastrengo (VR)\n
Via Vittorio Veneto	Via Vittorio Veneto - 37010 Pastrengo (VR)\n
Via Merano	Via Merano - 37010 Pastrengo (VR)\n
Via Pontara	Via Pontara - 37010 Pastrengo (VR)\n
Parco Montaer	Località Montaer\n""")

async def Villafranca(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("ALPO - VIA DON PROVOLO\nCALURI - VIA CALURI\nCALURI - VIA ALBINO LUCIANI\nCALURI\nDOSSOBUONO - VIA BRIGATE ALPINE\nDOSSOBUONO - VIA CAVOUR\nDOSSOBUONO - VIA DELLA MADDALENA ANGOLO VIALE EUROPA\nDOSSOBUONO - VIA DON BOSCO\nDOSSOBUONO -VIA VENETO\nDOSSOBUONO - VIA FRASSINI\n VIA PAOLO BEMBO DOSSOBUONO\nDOSSOBUONO - VIA ALESSANDRI\nDOSSOBUONO - VIA ALESSANDRI\nQUADERNI - VIA TITO SPERI\nQUADERNI - VERDE VIA SILVIO PELLICO\nQUADERNI - VIA AFRO DECO\nRIZZA - VIA ZUANETTI\nRIZZA - VIA ZUANETTI 2\nRIZZA - VIA DELL AMICIZIA\nROSEGAFERRO - VIA MONS. COMBONI\nROSEGAFERRO - VIA ZAMBONI\nVILLAFRANCA - VIA SPALLANZANI / VIA MALPIGHI\nVILLAFRANCA - PARCO DEL TIONE\nVIA ISONZO - EX IPPODROMO\nVILLAFRANCA - CASTELLO SCALIGERO\nVILLAFRANCA - VIA BROLI ANTICHI 1\nVILLAFRANCA - VIA CESARE MARCHI\nVILLAFRANCA - VIA BROLI ANTICHI 2\nVILLAFRANCA - VIA DONATORI DI SANGUE\nVILLAFRANCA - VIA FOGAGNOLO\nVILLAFRANCA - VIA DELL'ALPINO\n VILLAFRANCA - VIA DELL'ALPINO\nVILLAFRANCA - VIA PACE\nVILLAFRANCA - VIA DEL FANTE\nVILLAFRANCA - VIALE OLIMPIA\nVILLAFRANCA - VIA DANTE\nVILLAFRANCA - VIA ESPERANTO\nVILLAFRANCA - P.ZZA QUARTIERE MADONNA DEL POPOLO\nVILLAFRANCA - VIA BOTTAGISIO\nVILLAFRANCA - VIA EINAUDI\nVILLAFRANCA - VIA MARTINELLI\nVILLAFRANCA - VIA BUOZZI\nVILLAFRANCA - VIA VOLTURNO VIA CRISPI\nVILLAFRANCA - VIA BRESAOLA\nVILLAFRANCA - VIA DELLA SPERANZA\nVILLAFRANCA - VIA DELLA SPERANZA\nVILLAFRANCA - VIA MAGENTA\nVILLAFRANCA - VIA LABRIOLA\nVILLAFRANCA - VIA OLMO\nVILLAFRANCA - VIA MONTALE\nVILLAFRANCA - VIA COLLODI")

async def Castelnuovo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /hello is issued."""
    await update.message.reply_text("""
Parco Brolo delle Melanie	Via Castello, Via Manara e Via Pozzetto Castelnuovo del Garda\n
Parco 11 Aprile 1848	Via 11 Aprile 1848\n
Parco Campanello	Via Campanello\n 
Parco Ronchi	Via Verdi\n
Parco Centro Sociale Cavalcaselle	Via Mantovana\n
Parco dei Tavoli	Via Martin Luther King, Via Pacifico Perantoni\n
Parco Piazzale Chiesa Sandrà	Via Pastrengo\n
Parco cà Perari	Via Vigo\n
Parco Modigliani	Via Modigliani\n
Parco Volperara	Via Volperara\n
Parco Nicolis	Via Igino Nicolis\n
Parco Casal	Via Aldo Moro\n
Parco Giardi Pubblici Sandrà	Via De Gaspari, Via Einaudi, Via Corobbi\n
Parco Don Milani	Via Don Milani\n
Parco Oliveto	Via Oliveto\n
Parco Zonconi 	Via Zonconi, Via Edith Stein\n
Parco Cesare Marchi	Via Cesare Marchi\n
Parco Della Pace	Via Della Pace\n
Parco Pellico	Via Silvio Pellico\n
Parco Montello	Via Montello\n
Parco Rosselli	Via F.lli Rosseli Via Valbruna\n
Parco Polderin	Via Polderin\n
Parco D'Annunzio	Via D'annunzio\n
Parco Alberetti	Via Marco Polo, Via Alberetti\n
Parco Deledda	Via Grazia Deledda\n
Parco Serena	Via Mantovana\n
Parco Belvedere 1	Via Giovanni Paolo 2°\n
Parco Belvedere 2	Via Giovanni Paolo 2°\n
Parco Catullo	Via Catullo\n
Parco Giotto	Via Giotto\n
Parco Ferrari	Via Enzo Ferrari\n
Parco Pasteur	Via Louis Pasteur\n
Parco Camalavicina	Via Camalavicina\n
Parco Attila	Via Attila\n
Parco Risorgimento	Via Risorgimento\n
Piazza 24Giugno 1886	Piazza 24Giugno 1886\n
Parco 6 Fontane	Vicolo Fiume\n
Parco Mongabia	Via Costantino Nigra\n
Parco Impianti Sportivi Castelnuovo	Via Oregolo\n
Parco Impianti Sportivi Sandrà	Via S. Antonio\n
Parco Pasque Veronesi	Via Pasque Veronesi\n
Parco Martin Luther King	Via Martin Luther King\n
Parco Monte Alto	Via Degli Studi\n
"""
)


def main() -> None:
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("localita", localita))
    app.add_handler(CommandHandler("Valeggio", Valeggio))
    app.add_handler(CommandHandler("Sommacampagna", Sommacampagna))
    app.add_handler(CommandHandler("Sona", Sona))
    app.add_handler(CommandHandler("Palazzolo_di_sona", Palazzolo_di_sona))
    app.add_handler(CommandHandler("Lugagnano_di_sona", Lugagnano_di_sona))
    app.add_handler(CommandHandler("San_giorgio_in_salici", San_giorgio_in_salici))
    app.add_handler(CommandHandler("Pescantina", Pescantina))
    app.add_handler(CommandHandler("Mozzecane", Mozzecane))
    app.add_handler(CommandHandler("Pastrengo", Pastrengo))
    app.add_handler(CommandHandler("Villafranca", Villafranca))
    app.add_handler(CommandHandler("Castelnuovo", Castelnuovo))
    app.run_polling()

if __name__=='__main__':
   main()


