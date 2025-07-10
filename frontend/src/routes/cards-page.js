import { VStack, Heading, Text, Button } from "@chakra-ui/react";
import { useEffect, useState } from "react";
import { getCards } from "../endpoints/api";

const CardsPage = () => {
  const [cards, setCards] = useState([]);

  useEffect(() => {
    const fetchCards = async () => {
      const cardsData = await getCards();
      console.log("Cards data:", cardsData); // Отладка
      setCards(cardsData || []); // Если cardsData не массив, используем пустой массив
    };
    fetchCards();
  }, []);

  return (
    <VStack>
      <Heading> История </Heading>
      <VStack>
        {Array.isArray(cards) &&
          cards.map((card) => {
            return (
              <VStack>
                <Text key={card.id}>
                  {card.date_card} {card.first_name} {card.date_of_birth}{" "}
                  {card.address} {card.doctor?.first_name}{" "}
                  {card.doctor?.surname} {card.doctor?.last_name}
                </Text>
                <Button>Update</Button>
              </VStack>
            );
          })}
      </VStack>
    </VStack>
  );
};

export default CardsPage;
