<svelte:head>
	<script defer async
	src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAQdXjUnjQHJINv-x9Z_tLpSo7nL7_qo9o&callback=initMap">
	</script>
</svelte:head>

<script>
    
	import {Router, Route} from 'svelte-routing';
	import Signup from './Signup.svelte';
	import DashboardMap from './DashboardMap.svelte';
	import PostFeed from './PostFeed.svelte';
    import { GoogleAuthProvider } from 'firebase/auth';



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
    <!-- ... other routes -->
</Router>
