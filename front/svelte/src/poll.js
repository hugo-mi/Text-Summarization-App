/**
 * Module to run a function periodically
 */
import { onMount } from 'svelte';

/**
 * Periodically calls the function given in parameter.
 * 
 * @param {int} fn function to call periodically
 * @param {int} ms time between each call
 */
export function poll(fn, ms) {
    onMount(() => {
        const interval = setInterval(fn, ms);
        fn();

        return () => clearInterval(interval)
    });
}
