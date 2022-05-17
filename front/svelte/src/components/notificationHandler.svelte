<!-- Notification Handler. This component is added to every view and prompts notifications when processing records are finished -->
<script>
    import { poll } from "../poll.js";
    import { getNotificationsContext } from "svelte-notifications";
    const { addNotification } = getNotificationsContext();
    import { pendingRecords } from "./store.js";

    /**
     * Prompts a notification that a record is finished, with a link to access it.
     * @param id
     */
    function notifyRecordCompletion(id) {
        addNotification({
            text: `CR numéro ${id} disponible`,
            position: "bottom-left",
            type: "success",
            id: id,
            removeAfter: 8000
        });
    }

    /**
     * Periodically updating of the pending records' status and placing them in the local store.
     * If the record is done, it is removed from the store and a Notification is prompted to the user.
     */
    poll(function fetchRecordsStatus() {
        for (const [key, value] of $pendingRecords.entries) {
            fetch(`http://localhost:8080/api/summary/${key}`).then(
                async (response) => {
                    const summary = await response.json();
                    $pendingRecords.set(key, summary.status);
                    for (const [key, value] of $pendingRecords.entries) {
                        console.log(
                            "fetched Record number ",
                            key,
                            ", status : ",
                            value
                        );
                        if (value == "done") {
                            console.log(
                                "Record number ",
                                key,
                                " has been summarized"
                            );
                            notifyRecordCompletion(key);
                            $pendingRecords.remove(key);
                        }
                    }
                }
            );
        }
    }, 3000);
</script>
