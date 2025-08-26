import { useEffect, useState } from "react";
import { getCard } from "../endpoints/api";

export const useCard = (card_id) => {
  const [card, setCard] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCard = async () => {
      try {
        const card = await getCard(card_id);

        if (card) {
          setCard(card);
        } else {
          setError("Карта не найдена");
        }
      } catch (err) {
        setError("Ошибка загрузки данных" + err.message);
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchCard();
  }, [card_id]);

  return { card, loading, error };
};
