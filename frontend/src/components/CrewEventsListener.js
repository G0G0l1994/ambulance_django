import { useEffect } from "react";
import { useToast } from "@chakra-ui/react";
import { useAuth } from "../contexts/useAuth";

// Формируем адрес бэкенда для SSE динамически: тот же hostname, порт 8000
const EVENTS_URL = `${window.location.protocol}//${window.location.hostname}:8000/events/`;

const CrewEventsListener = () => {
  const { myCrew } = useAuth();
  const toast = useToast();

  useEffect(() => {
    if (!myCrew?.crew_number) return;

    const channel = `crew-${myCrew.crew_number}`;
    // Добавляем и channel, и channels для совместимости с разными версиями django-eventstream
    const q = `channel=${encodeURIComponent(
      channel
    )}&channels=${encodeURIComponent(channel)}`;
    const url = `${EVENTS_URL}?${q}`;

    const es = new EventSource(url);

    es.onopen = () => {
      // eslint-disable-next-line no-console
      console.log("SSE opened:", url);
    };

    // django-eventstream отправляет именованные события (event: new_call)
    es.addEventListener("new_call", (e) => {
      try {
        const payload = JSON.parse(e.data);
        if (payload?.type === "card_assigned") {
          toast({
            title: "Новый вызов",
            description: `Карта № ${payload.card_id}`,
            status: "info",
            duration: 5000,
            isClosable: true,
          });
          window.dispatchEvent(
            new CustomEvent("incoming-call", { detail: payload })
          );
        }
      } catch {}
    });

    // Резервный обработчик на случай unnamed событий
    es.onmessage = (e) => {
      try {
        const payload = JSON.parse(e.data);
        if (payload?.type === "card_assigned") {
          window.dispatchEvent(
            new CustomEvent("incoming-call", { detail: payload })
          );
        }
      } catch {}
    };

    es.onerror = (e) => {
      console.warn("SSE error", e);
    };

    return () => {
      es.close();
    };
  }, [myCrew, toast]);

  return null;
};

export default CrewEventsListener;
