import { VStack, Heading, Text, Button, Spinner } from "@chakra-ui/react";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import { getCardsDoctorList, getProfile } from "../endpoints/api";

const CardsHistory = () => {
  const [cards, setCards] = useState([]);
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const userData = await getProfile();
        setUser(userData);

        if (userData && userData.id) {
          const cardsData = await getCardsDoctorList(userData.id);
          setCards(Array.isArray(cardsData) ? cardsData : []);
          console.log(cardsData[0].diagnosis_data);
        }
      } catch (error) {
        console.error("Ошибка загрузки данных:", error);
        setCards([]);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <Spinner size="xl" />;
  }

  return (
    <VStack>
      <Heading>История вызовов</Heading>
      <VStack spacing={4} align="stretch" w="100%">
        {cards.length === 0 ? (
          <Text>Нет доступных карт</Text>
        ) : (
          cards.map((card) => (
            <VStack
              key={card.id}
              align="start"
              borderWidth={1}
              borderRadius="md"
              p={4}
            >
              <Text>
                <b>Дата:</b> {card?.datetime_data?.date_card}
              </Text>
              <Text>
                <b>Пациент:</b> {card.patient?.full_name}{" "}
                {card.patient?.date_of_birth &&
                  `(д.р. ${card.patient.date_of_birth})`}
              </Text>
              <Text>
                <b>Бригада:</b> {card.crew}
              </Text>
              <Text>
                <b>Причина:</b> {card.cause}
              </Text>
              <Text>
                <b>Врач:</b> {card.doctor?.last_name} {card.doctor?.first_name}{" "}
                {card.doctor?.surname}
              </Text>
              <Text>
                <b>Статус:</b> {card.status}
              </Text>
              {card?.diagnosis_data && (
                <VStack align="start">
                  <Text>
                    <b>МКБ-10:</b> {card?.diagnosis_data?.mkb}
                  </Text>
                  <Text>
                    <b>Диагноз:</b> {card?.diagnosis_data.diagnosis}
                  </Text>
                </VStack>
              )}

              <Button onClick={() => navigate(`/cards/${card.id}/update`)}>
                Редактировать
              </Button>
            </VStack>
          ))
        )}
      </VStack>
    </VStack>
  );
};
export default CardsHistory;
