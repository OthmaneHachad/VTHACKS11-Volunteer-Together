<script>
    
	import {Router, Route} from 'svelte-routing';
	import Signup from './Signup.svelte';
	import DashboardMap from './DashboardMap.svelte';
	import PostFeed from './PostFeed.svelte';
    import ProfilePage from './profilePage.svelte';
</script>



<style>
	:global(body) {
		padding: 0;
	}
</style>


<Router>
    <Route path="/" component={Signup} />
	<Route path="/dashboardMap" component={DashboardMap} />
	<Route path="/feed" component={PostFeed} />
	<Route path="/profilePage" component={ProfilePage} />
    <!-- ... other routes -->
</Router>
