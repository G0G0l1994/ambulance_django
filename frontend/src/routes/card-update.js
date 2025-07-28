import CardLayout from "../components/CardLayout";
import { useParams } from "react-router-dom";
import { useCard } from "../hook/useCard";

const CardUpdate = () => {
  const { card_id } = useParams();
  console.log(card_id);
  const { card, loading, error } = useCard(card_id);
  console.log(card);
  console.log(error);
  if (loading) return <div>Загрузка...</div>;
  if (error) return <div>Ошибка: {error}</div>;
  if (!card) return <div>Карта не найдена</div>;

  return <CardLayout card_id={card_id} />;
};

export default CardUpdate;
