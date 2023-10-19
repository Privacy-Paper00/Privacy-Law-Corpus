Privacy Law Corpus Manual V1.1 Release – October 19, 2023 

Usage Information
The corpus metadata is made available under a Creative Commons Attribution-NonCommercial-ShareAlike 2.0 Generic license (CC BY-NC-SA 2.0). Inquiries about commercial licensing should be directed to [Anonymized]. If you use the corpus (i.e., the collection of documents or the metadata) toward a publication, you must cite the following work:
[Anonymized]. URL: [Anonymized]
The above work is also important for understanding the structure and contents of the corpus.

The corpus is provided as-is, without guarantees of reliability or completeness. For questions about the corpus, please contact [Anonymized]. 

Version History
[October 19, 2023]: The second release (V1.1) of the Privacy Law Corpus, corresponding with imminent release of the work
[June 20, 2022]: The first release (V1.0) of the Privacy Law Corpus, corresponding with imminent release of the work

Overview
This corpus contains a collection of Privacy Laws (e.g., laws, guidelines, orders, etc.) from around the world, mostly issued by national-level governments, but also occasionally from super-national organizations or subnational entities. The oldest Privacy Laws in the set is from 1860, and the newest from 2020. They were manually gathered from the world wide web by members of the research team. Researchers sought guidance from several law information websites, as represented by the URLs in the Document Source column as well as the Starting Source column.

A .csv file contains the metadata for the corpus: this is a large table with information about each Privacy Law. Each Privacy Law is provided in multiple formats, including translations to English when possible. Some translations of Privacy Laws to English were found on the web, and some were created by the researchers using automated online tools. The reliability of translations in the dataset is not guaranteed.

The corpus download contains the following subdirectories and files:
- [Privacy-Law-corpus]: Contains the contents of the entire corpus and related documents.
    - [corpus_documents]: Versions of all of the documents in the corpus ("Privacy Laws", interchangably).
        - [pdf_files]: PDF versions of all of the documents in the corpus. The documents in this directory were not used for analysis in the paper.
            - [english_pdf_files]: All PDF documents in the English language.
                - [english_translated_pdf_files]: PDFs of all Privacy Laws that were not originally found in English and required translation to English, using a third party translation service. 
                - [original_english_pdf_files]: PDFs of all Privacy Laws that were originally found in English.
            - [non_english_pdf_files]: PDFs of Privacy Laws that were not originally found in English, provided in their original respective languages.
        - [plain_text_files]: TXT versions of all of the documents in the corpus. The documents in this directory were used for analysis in the paper.
            - [english_text_files]: All TXT documents in the English language.
                - [english_translated_text_files]: TXTs of all Privacy Laws that were not originally found in English and required translation to English, using a third party translation service. 
                - [original_english_text_files]: TXTs of all Privacy Laws that were originally in English.
            - [non_english_text_files]: TXTs of Privacy Laws that were not originally in English, provided in their original respective languages.
    - [Privacy_Law_corpus_metadata.csv]: Metadata for Privacy Laws in CSV format.
    - [Privacy_Law_corpus_metadata.xlsx]: Metadata for Privacy Laws in excel format.
    - [readme.txt]: This file; documentation for the corpus.

Metadata Columns

The metadata file contains the following columns:

Jurisdiction Name
Column Description: This column contains the name of the jurisdiction this document applies to. 
Notes: There are documents included in the corpus that apply to more than one country from the legislating bodies of Denmark/Greenland, Netherlands/Caribbean, and Serbia/Bosnia Herzegovina/Kosovo.

Key Law Original Title
Column Description: This column contains the original language title of the document described in this record. In the case of documents originally presented in English, the English title is presented here.

Key Law Corpus Identifier
Column Description: This column contains the file name of the document present in the corpus.

Key Law English Translated Title
Column Description: This column contains the English language translated title of the document described in this record, if the original language of this record is one other than English. 
Values: If the original language of this document is English, this cell may contain the value [Not Applicable].

In Effect/Repealed/NYiF (Not Yet in Force)
Column Description: This column describes whether the law is currently in effect, and, if it is not, whether it has been revoked in some way or it is not yet in force.
Values: In Effect, Repealed, Not Yet in Force (NYiF)

Originally Passed
Column Description: This column labels what country or body of agreement the jurisdiction was originally passed in. 

Currently Applicable 
Column Description: This column labels what country or body of agreement the jurisdiction currently applies to.

Sector: Public, Private, or Both (From Greenleaf Tables)
Column Description: From Graham Greenleaf’s Global Tables of Data Privacy Laws and Bills, certain documents provided were labeled as covering the public sector only, the private sector only, or both sectors. The documents not gathered by the tables were labeled as not applicable.
Values: Public, Private, Both, [Not Applicable]

First Privacy Law
Column Description: The date of the enactment of the first privacy law.

This Law Promulgated
Column Description: This column represents date promulgated rather than enacted. 
Notes: Although these two dates are usually the same, there were a few documents that were Not Yet in Force (NYiF), and this column contains promulgation rather than enactment dates. Within this corpus, there are a few NYiF documents that have been promulgated but not enacted.

Last: Latest Revision
Column Description: The date of the latest revision of the document, if any. 
Notes: If no revision had occurred or was applicable, then the date of the law promulgated was applied for the document. 

International Agreements (From Greenleaf Tables)
Column Description: Any agreements between countries that involves legal obligations
Values: [Not Applicable]; Not-UN, ICCPR; ICCPR+OP; CoE108(RP); CoE108(AI); CoE108+(S); EU(Adq); EU(M); EU(OCT); CPTPP(R); CBPRs(S); GDPR(Adq); AUConv(S)

Member (From Tables)
Column Description: This column is used for countries involved in any regional groupings relevant to data privacy.
Values: [Not Applicable]; CoE; AU; SADC; ECCAS; CARICOM; OECS; MERCOSUR; APEC; OECD; CARICOM (Assoc.); UKOT; SAARC; EU; ECOWAS; GPEN; CEMAC; None: UK Crown Dependency; EEA; ASEAN; None: Self-governing, not UK; ECOWAS (A); NAFTA; US FTA

Original Language:
Column Description: The language that the jurisdiction is originally provided in is considered the original language.
Notes: Some jurisdictions provided multiple languages and so both languages were collected and noted.

Document Source: Original
Column Description: The source of where the document was collected in the form of a URL in its original language. These URLs are the direct path to accessing the document in its most raw version.
Notes: Documents labeled as [None] in this column were originally in English and placed under the Document Source: English column 

Government Website?
Column Description: This column labels whether the source of the website providing the jurisdiction is from a governmental website or not.
Values: Y; N
Notes: Websites ending in .gov or with a country domain were considered governmental websites. For this column, it is understood that Y stands for yes and N stands for no.

Document Source: English
Column Description: The source of where the document was collected in the form of a URL in a translated English version if the original language was not English. These URLs are the direct path to accessing the document in its most raw version.
Notes: Documents labeled as [None] in this column do not have a translation in English for the document source URL. 

Translation Type
Column Description: If a jurisdiction was not originally in English, it was further separated into three other categories of translation type: official translation provided by the source, unofficial translation provided by the source, or translated by researchers with a non-government machine.
Values: [Not Applicable]; Official Translation; Non-Government Machine; Unofficial Translation

Starting Source
Column Description: Oftentimes, it would take an initial starting website to find the URL containing the document. This column is for the websites used to narrow down and find the location of the document. 
Notes: Any documents labeled as [None] did not have a starting source. 

Plain Text File Directory File Path
Column Description: This column describes the location of the original / English language translated document (if applicable) text file within the corpus directory structure.

Date of Retrieval of Original
Column Description: This column lists the date that the original document source file was downloaded from its source.

Date of Retrieval of English Translation
Column Description: This column lists the date that the English language translated document (if applicable) source file was downloaded from its source; if this is a machine translation with no source document available, this is the date that the English language machine translated text was saved in the corpus.

Comments/Notes
Column Description: This column includes any comments or notes from the researchers compiling the data. This may include: notes regarding whether a particular piece of legislation repeals or amends another listed piece of legislation, whether a particular piece of legislation enacts, instates, or augments an international agreement, miscellaneous notes regarding the document languages and sources, etc.

Acknowledgments

We acknowledge Prof. Graham Greenleaf’s itemization of privacy laws as an inspiration for our work: Global Tables of Data Privacy Laws and Bills (7th Ed, January 2021); Global Tables of Data Privacy Laws and Bills (6th Ed, January 2019). Work on this corpus began with collecting the set of laws that his paper refers to, and it continued outward from that set. We are also grateful to Prof. Greenleaf for his correspondence while building this corpus.

This corpus was developed by researchers at the [Anonymized] and was funded by NSF grant [Anonymized], [Anonymized], and [Anonymized], “[Anonymized]”. 

