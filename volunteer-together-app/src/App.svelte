<script>
    
	import {Router, Route} from 'svelte-routing';
	import Signup from './Signup.svelte';
	import DashboardMap from './DashboardMap.svelte';


    


</script>


<Router>
    <Route path="/" component={Signup} />
	<Route path="/dashboardMap" component={DashboardMap} />
    <!-- ... other routes -->
</Router>
