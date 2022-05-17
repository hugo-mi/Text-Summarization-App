<script>
	import Router from "svelte-spa-router";
	import Navbar from "./components/navbar.svelte";
	import Footer from "./components/footer.svelte";
	import ScrollToTop from './components/scrollToTopButton.svelte';
	import Notifications from "svelte-notifications";
	import notificationItem from "./components/notificationItem.svelte";
	import Notification from "./components/notificationHandler.svelte";

	// Import the list of routes
	import routes from "./routes";

</script>

<Notifications item={notificationItem}>
	<Navbar />
	<Notification />
	<Router {routes} />
	<Footer />
	<ScrollToTop />
</Notifications>
