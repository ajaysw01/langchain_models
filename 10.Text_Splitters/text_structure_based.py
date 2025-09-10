from langchain.text_splitter import  RecursiveCharacterTextSplitter


text = """
Artificial intelligence (AI) refers to the ability of a machine to learn patterns and make predictions. AI does not replace human decisions; instead, AI adds value to human judgment. 

What is the difference between AI and augmented intelligence?
Augmented intelligence has a modest goal of helping humans with tasks that are not practical to do. For example, “reading” 1000 pages in an hour. In contrast, artificial intelligence has a lofty goal of mimicking human thinking and processes.
Intelligence types : 
1. Human 
2. Artificial  : It is there to replace human intelligence.
3. Augmented : here both machine and human work together. s like screen readers for the blind,
voice-driven navigation, or my in-car collision avoidance system
I submit to you that my drive from my home to my office used 3 forms of intelligence. The first
intelligence was human intelligence. The intelligence there was the intelligence that I needed to operate
the vehicle, to turn the steering wheel, to check my mirrors.
The second form of intelligence was artificial intelligence. Once I got on the highway, I turned on the
self-driving feature in my car. Fancy. Now the car stayed in its own lane, kept an appropriate distance
from the vehicle in front, and maintained a proper speed. No input from me at all.
When I got off of the highway, I used a third form of intelligence: augmented intelligence. Augmented
intelligence, well, that took the form of all the driver-assist features in the vehicle, things like collision
detection, to alert me if I got too close to the csr
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
)

chunks = splitter.split_text(text)

print(chunks)
print(len(chunks))