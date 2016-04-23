class Symptoms:
    
    # a - prefix for allergy
    # f - prefix for flue
    symptoms = {
                "a0": "Sneezing",
                "a1": "Runny or stuffy nose",
                "a2": "Red, itchy or teary eyes",
                "a3": "Tightness in the chest",
                "a4": "Shortness of breath",
                "a5": "Wheezing, coughing",
                "a6": "Itching"
                }
    
    
    def get_symptoms(self):
        return self.symptoms
    
    def get_symtoms_fb(self):
        s = []

        for k, v in self.symptoms.iteritems():
            s.append({"type": "postback", "title": v, "payload": k})
            
        return s    
