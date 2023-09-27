import tweetnlp 
model1 = tweetnlp.load_model('sentiment')
tsen=model1.sentiment("Ishan Kishan not happy about getting out when set")
print(tsen)