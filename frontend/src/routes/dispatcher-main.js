import { useState, useEffect } from "react";
import { VStack, Heading, Button, Select, HStack } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";
import { Text } from "@chakra-ui/react";
import { getCardsList, assignCard, getProfile } from "../endpoints/api";
import { columns } from "../constants/table-fields";
import { CardTable } from "../components/card.table";

const DispatcherMain = () => {
  const [cards, setCards] = useState([]);

  const fetchCards = async () => {
    const cardsData = await getCardsList();
    setCards(Array.isArray(cardsData) ? cardsData : []); // Если cardsData не массив, используем пустой массив
  };

  useEffect(() => {
    fetchCards();
  }, []);

  const handleCardUpdate = () => {
    fetchCards();
  };

  return (
    <VStack>
      <Heading> Диспетчерская </Heading>
      <VStack spacing={4} align="stretch" w="100%">
        <CardTable
          columns={columns}
          cards={cards}
          onCardUpdate={handleCardUpdate}
        />
      </VStack>
    </VStack>
  );
};

export default DispatcherMain;
