namespace * airr

/* AIRR DATA TYPES */

struct Study {
    // The study ID
    1: optional string id

    // The study title
    2: optional string title

    // How the study will be performed (OBI_0500000) (e.g., placebo controlled
    // phase 3 clinical trial)
    3: optional string type

    // Study inclusion/exclusion criteria (OBI_0500027)
    4: optional string criteria

    // Grant funding agency
    5: optional string funding

    // The name of the lab or institution
    6: optional string lab

    // Contact information for the study's corresponding author
    7: optional string authorContact

    // Contact information for the person that uploaded the data
    8: optional string uploaderContact

    // Contact information for the lab
    9: optional string labAddress

    // DOIs for relevant publications or other documents
    10: optional list<string> dois
}

enum Origin {
    HUMAN,
    ANIMAL,
    SYNTHETIC,
    UNKNOWN
}

enum Sex {
    MALE,
    FEMALE,
    UNKNOWN
}

struct Subject {
    // The subject ID
    1: optional string id

    // The Origin of the subject
    2: optional Origin origin

    // The sex of the subject
    3: optional Sex sex

    // The age of the subject
    4: optional i64 age

    // The unit for the age value
    5: optional string ageUnit

    // The qualitative age, e.g., "adult"
    6: optional string ageQual

    // The experimental event at which the age is valid (e.g., enrollment, T0)
    7: optional string ageEvent

    // The ancestry population of the subject
    // http://www.allelefrequencies.net/datasets.asp#tag_4
    8: optional string ancestry

    // The ethnicity of the subject
    9: optional string ethnicity

    // The race of the subject
    10: optional string race

    // The name of a species (typically a taxonomic group) of organism
    11: optional string species

    // The name of a strain of an organism variant
    12: optional string strain

    // Subject IDs for other subjects this subject is linked to
    13: optional list<string> links

    // Subject IDs for other subjects this subject is linked to
    14: optional list<string> linkTypes
}

struct DiagnosisIntervention {
    // The diagnosis or intervention ID
    1: optional string id

    // Experimental group (e.g., case vs control)
    2: optional string studyGroupDescription

    // Defined pathologic process with characteristic signs and symptoms
    3: optional string diagnosis

    // Years since diagnosis
    4: optional string diseaseLength

    // Position in the normal progression of the disease (ex. tumor, nodes,
    // mets)
    5: optional string diseaseStage

    // Prior Therapies for the Primary Disease under study (e.g., surgery,
    // medication, etc)
    6: optional list<string> priorTherapies

    // Material entitity to which the host's immune system came into contact
    // during the immunological process (e.g., vaccine).
    7: optional string immunogen

    // Drug, Vaccine, Surgery etc.
    8: optional string intervention

    // Relevant clinical history
    9: optional string pastMedicalHistory
}

struct Sample {
    // The sample ID
    1: optional string id

    // The sample type (e.g. tissue, body fluid)
    2: optional string type

    // The sample anatomic site (e.g., spleen)
    3: optional string anatomicSite

    // The disease state of the sample (e.g., tumor vs margin)
    4: optional string diseaseState

    // Sample collection time delta relative to collection time event (T0)
    5: optional string time

    // Collection time event (datetime)
    6: optional string T0

    // Source of the sample (if from a commercial source)
    7: optional string source
}

// *** DO WE NEED A LIBRARY OBJECT? Is it the Sample? ***

enum Substrate {
    DNA,
    RNA
}

struct ExperimentalProcessing {
    // The processing ID
    1: optional string id

    // Enzymatic digestion and/or physical methods used to isolate cells from
    // sample
    2: optional string tissueProcessing

    // e.g., cryopreservation
    3: optional string cellStorage

    4: optional string cellViability

    5: optional string cellYield

    // e.g., flow cytometry, magnetic bead enrichment, etc.
    6: optional string cellIsolation

    // e.g., overnight culture, cytokine stimulation, etc.
    7: optional string cellStimulation

    // Cell subset designation; list of markers for flow sorting; fcs files
    8: optional string cellSubset

    // Single cell or bulk?
    9: optional bool singleCell

    10: optional i64 numCells

    11: optional i64 cellsPerRun

    12: optional Substrate substrate

    13: optional string dnaQuality

    14: optional string rnaQuality

    // e.g., RACE, nested amplification
    15: optional string libraryGenerationMethod

    // e.g., enzymes used, PCR protocol
    16: optional string libraryGenerationProtocol

    // e.g., constant region vs V region amplification
    17: optional string targetLocus

    // e.g., poly-A, GSP, etc
    18: optional string reverseTranscriptionTarget

    // **this probably needs far more structure** describe set up of barcodes
    19: optional string barcodes

    // **this probably needs far more structure** describe set up of UMIs
    20: optional string umis

    // e.g., FR1
    21: optional string forwardPCRPrimerLocation

    // e.g., FR1
    22: optional string reversePCRPrimerLocation

    23: optional list<string> forwardPCRPrimerSequences

    24: optional list<string> reversePCRPrimerSequences

    // Does the amplicon capture the full VDJ or only part of it?
    25: optional bool partial

    // heavy vs light vs paired
    26: optional string chainCapture

    // nanograms of template into primary amplification
    27: optional i64 ngTemplate

    // number of reads passing QC
    28: optional i64 passingReads

    29: optional string internalControls

    30: optional list<string> protocolIds

    31: optional string sequencingPlatform

    // ** too small **
    32: optional list<i32> readLengths

    33: optional string sequencingFacility

    34: optional string batchId

    35: optional string sequencingDateTime

    36: optional string sequencingKit
}

struct SoftwareProcessing {
    // The software processing ID
    1: optional string id

    // List of software tools used
    2: optional list<string> tools

    // List of version numbers
    3: optional list<string> versions

    // How paired end data were assembled (**fold into tools?**)
    4: optional string pairedAssembly

    // **needs more structure?**
    5: optional string qualityThresholds

    // **needs more structure?**
    6: optional string primerMatchCutoffs

    // Method used to collapse multiple raw sequences into a single processed
    // sequence
    7: optional string collapsingMethod

    // General description of how QC is performed
    8: optional string dataProcessingProtocols
}

struct Rearrangement {
    1: optional string id

    2: optional string v

    3: optional string d

    4: optional string j

    5: optional string cdr3
}
