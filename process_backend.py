
class ProcessBackEnd:

    def init_process(self):
        try:
            for i in range (0,100,10):
                print(f"process {i}")
        except Exception as e:
            print (e)

ProcessBackEnd().init_process()            