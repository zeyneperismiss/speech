#Robot listens to speaker and stores what they say as variable 'text'

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration = 2)
    print('adjusted')
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
    except:
        print('Repeat please')
        
    if text == 'activate voice control':
        
        with sr.Microphone() as source:
            #r.adjust_for_ambient_noise(source, duration = 2) #records background noise for 1 second and adjusts to this noise level
            print('Speak Anything: ')
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                print('You said: {}'.format(text))
            except:
                print('Sorry could you please repeat that')

        #Robot gives reply in response to certain phrases or commands
                
        if text == 'hello':
            reply = 'hello to you too'
            print(reply)
            
        if text == 'grab the TV remote':
            reply = 'Ok, fetching the TV remote'
            print(reply)

            
