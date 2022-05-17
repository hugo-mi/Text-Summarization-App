import Home from './routes/Home.svelte'
import VoirCR from './routes/VoirCR.svelte'
import HistoriqueCR from './routes/HistoriqueCR.svelte'
import GenerateCR from './routes/GenerateCR.svelte'
import EditCR from './routes/EditCR.svelte'
import SearchCR from './routes/SearchCR.svelte'

export default {
	// Exact path
	'/': Home,
    '/VoirCR/:id/:isCreated?': VoirCR,
	'/HistoriqueCR': HistoriqueCR,
	'/GeneratorCR/': GenerateCR,
	'/EditCR/:type/:id/': EditCR,
	'/SearchCR/': SearchCR,
}
