from bardapi import Bard
import os
os.environ["_BARD_API_KEY"] = "bggoE2FdeHrX-GP0laq1s5Z8SaZ1iR-Q9ZEuWqOQDhsajy3uGccB1-Mi5xDn48yAHXSeCw."
message = input("enter:  ")    
print(Bard().get_answer(str(message)['content']))