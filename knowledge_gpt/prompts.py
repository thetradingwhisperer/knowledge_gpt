# flake8: noqa
from langchain.prompts import PromptTemplate

## Use a shorter template to reduce the number of tokens in the prompt
template_QA = """Create a final answer to the given questions using the provided document excerpts(in no particular order) as references. ALWAYS include a "SOURCES" section in your answer including only the minimal set of sources needed to answer the question. if you are unsure about the answer, give your best guest given the document provided as reference.

---------

QUESTION: When was the well spudded?
=========
Content: The well was cleaned up between 23:45 hrs on 29 Se ptember and 09:40 hrs on 30 September. The well was then opened at 10:35 hrs on 30 September and beaned up to a 1” choke. The well flowed on this choke setting until it was shut in at 14:00 hrs on 2 October. 
source: well_report.pdf
Content: Total Depth, 13,941 ft MDRT : 2,940,541.28 m N (UTM) 3,037 ft TVDRT 596,211.72 m E RT Elevation : 102 ft amsl. Water Depth : 205 ft bmsl. Well Status : Injecting/n2I.2 Drilling Operations I.2.1 Summary of Drilling Operations The derrick was skidded from slot AA-11 to AA-09. A 23" motor BHA was made up and the well was spudded at 13:30 hours on August 4, 1996. The 23" hole was drilled from the seabed at 307 ft to 977 ft, sweeping with 50 bbl HI-VIS pills and running Magnetic Single Shot gyro for every stand.
Document: end_of_well.pdf
Content: The string was pulled and a more 'aggressive' building assembly was run in hole. However, it was still not possible to build angle. A 62 bbl cement plug was sputted at 9864 ft but it was not possible to kick of on it. A 65 bbl plug was set at 8924 ft and the well was kicked off at 8450 ft. The well was drilled to 10911 ft where the Upper Nahr Umr Shale was encountered without being able to get it back down.
Document: new_operation.pdf
=========
FINAL ANSWER: The well was spudded at 13:30 hours on August 4, 1996.
Document: well_report.pdf

---------

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""

## Use a shorter template to reduce the number of tokens in the prompt
template_AQA = """Create a final answer to the given user question using the provided document excerpts(in no particular order) as references. ALWAYS include a "SOURCES" section in your answer including only the minimal set of sources needed to answer the question. if you are unsure about the answer, give your best guest given the document provided as reference.

---------

QUESTION: Fill in the a table with info for wellA and wellB. Info: spud or drilling start date, Reservoir name, logging tools?
=========
Content: The well was drilled on 30 September 2021. the TD was in the reservoir Madud, with the pressure log data taken from RFT. The well flowed on this choke setting until it was shut in at 14:00 hrs on 2 October. 
source: well_report_wellA.pdf
Content: Total Depth, 13,941 ft MDRT : 2,940,541.28 m N (UTM) 3,037 ft TVDRT 596,211.72 m E RT Elevation : 102 ft amsl. The well started on 12 January 2001. the TD was in the reservoir Namh, with the pressure log data taken from RFT. The well flowed on this choke setting until it was shut in on March 5. 
Document: well_report_wellB.pdf
Content: The string was pulled and a more 'aggressive' building assembly was run in hole. However, it was still not possible to build angle. A 62 bbl cement plug was sputted at 9864 ft but it was not possible to kick of on it. A 65 bbl plug was set at 8924 ft and the well was kicked off at 8450 ft. The well was drilled to 10911 ft where the Upper Nahr Umr Shale was encountered without being able to get it back down.
Document: new_operation.pdf
=========
FINAL ANSWER: Wellname, Drilled date, Reservoir, logging tools, Source
WellA, 30 September 2021, Madud , RFT, well_report_wellA.pdf
WellB, 12 January 2001, Namh, RFT, well_report_wellB.pdf
---------

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""


STUFF_PROMPT = PromptTemplate(
    template=template_AQA, input_variables=["summaries", "question"]
)
