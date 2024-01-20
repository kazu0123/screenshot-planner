import { isNotNullish } from "./isNotNullish";

export type CalendarEvent = {
    event_title: string,
    event_description: string,
    event_location: string,
    start_datetime: string,
    end_datetime: string,
    recurrence: string,
};

export const isCalendarEvent = (item: unknown): item is CalendarEvent => {
    if (!isNotNullish(item)) return false;

    return (
        typeof (item.event_title) === "string" &&
        typeof (item.event_description) === "string" &&
        typeof (item.event_location) === "string" &&
        typeof (item.start_datetime) === "string" &&
        typeof (item.end_datetime) === "string" &&
        typeof (item.recurrence) === "string"
    )
}
