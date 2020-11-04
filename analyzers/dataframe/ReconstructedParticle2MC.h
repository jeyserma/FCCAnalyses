
#ifndef  RECONSTRUCTEDPARTICLE2MC_ANALYZERS_H
#define  RECONSTRUCTEDPARTICLE2MC_ANALYZERS_H

#include <cmath>
#include <vector>

#include "ROOT/RVec.hxx"
#include "edm4hep/ReconstructedParticleData.h"
#include "edm4hep/MCParticleData.h"
#include "podio/ObjectID.h"
#include "TLorentzVector.h"

/// Return the D0 of a track to a reconstructed particle
std::vector<float> getRP2MC_p (std::vector<podio::ObjectID> recin,
			       ROOT::VecOps::RVec<podio::ObjectID> mcin,
			       ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> reco,
			       ROOT::VecOps::RVec<edm4hep::MCParticleData> mc);

/// Return the D0 of a track to a reconstructed particle
std::vector<float> getRP2MC_p_test (ROOT::VecOps::RVec<int> recin,
				    ROOT::VecOps::RVec<int> mcin,
				    ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData> reco,
				    ROOT::VecOps::RVec<edm4hep::MCParticleData> mc);



#endif
