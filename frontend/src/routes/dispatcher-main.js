import { useState, useEffect } from "react";
import { VStack, Heading, Button, Select, HStack } from "@chakra-ui/react";

import { getCardsList, assignCard, getProfile } from "../endpoints/api";
import { columns } from "../constants/table-fields";
import { CardTable } from "../components/card.table";

const DispatcherMain = () => {
  const [cards, setCards] = useState([]);
  const [pagination, setPagination] = useState({ next: null, prev: null });

  const fetchCards = async (url = null) => {
    const cardsData = await getCardsList(url);
    setCards(Array.isArray(cardsData?.results) ? cardsData?.results : []);

    setPagination({
      next: cardsData?.next || null,
      prev: cardsData?.previous || null,
    });
  };

  useEffect(() => {
    fetchCards();
  }, []);

  const handleCardUpdate = () => {
    fetchCards();
  };
  const handleNextPage = async () => {
    if (pagination.next) {
      const relativeUrl =
        new URL(pagination.next).pathname + new URL(pagination.next).search;
      fetchCards(relativeUrl);
    }
  };

  const handlePrevPage = async () => {
    if (pagination.prev) {
      const relativeUrlPrev =
        new URL(pagination.prev).pathname + new URL(pagination.prev).search;
      fetchCards(relativeUrlPrev);
    }
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
      <HStack spacing={4}>
        <button onClick={handlePrevPage}>prev</button>
        <button onClick={handleNextPage}>next</button>
      </HStack>
    </VStack>
  );
};

export default DispatcherMain;
