
class ProcessBackEnd:

    def init_process(self):
        try:
            for i in range (0,100,10):
                print(f"Init process {i}")                
        except Exception as e:
            print (e)

    def finish_process(self):
        try:
            for i in range (0,100,10):
                print(f"End process {i}")                
        except Exception as e:
            print (e)            

ProcessBackEnd().init_process()
ProcessBackEnd().finish_process()