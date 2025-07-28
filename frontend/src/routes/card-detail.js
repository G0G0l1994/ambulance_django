import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { getCard } from "../endpoints/api";
import { useNavigate } from "react-router-dom";
import { Button, HStack, VStack, Text } from "@chakra-ui/react";
import { useCard } from "../hook/useCard";

const CardDetail = () => {
  const { card_id } = useParams();

  const navigator = useNavigate();

  const { card, loading, error } = useCard(card_id);

  if (loading) return <div>Загрузка...</div>;
  if (error) return <div>{error}</div>;
  if (!card) return <div>Карта не найдена</div>;

  return (
    <VStack className="card-detail">
      <h2>Карта вызова №{card.id}</h2>

      <HStack>
        <Text fontWeight="bold">Пациент:</Text>
        <p>
          {card.patient.full_name} ({card.patient.full_age} лет)
        </p>
        <Text fontWeight="bold">Дата рождения: </Text>
        <Text>
          {new Date(card.patient.date_of_birth).toLocaleDateString("ru-ru")}
        </Text>
      </HStack>

      <VStack>
        <Text fontWeight="bold">Основная информация:</Text>
      </VStack>
      <HStack>
        <Text>Повод вызова: {card.cause}</Text>
        <Text>Бригада: {card.crew ? card.crew : "Отсутствует"}</Text>
        <p>Адрес: {card.address ? card.address : "Отсутствует"}</p>
      </HStack>

      {card.datetime_data && (
        <HStack>
          <h3>Временные метки</h3>
          <p>
            Дата карты:{" "}
            {new Date(card.datetime_data.date_card).toLocaleDateString("ru-ru")}
          </p>
          <p>
            Время приема вызова:{" "}
            {new Date(card.datetime_data.time_of_receipt).toLocaleTimeString(
              "ru-ru"
            )}
          </p>
        </HStack>
      )}

      {card.diagnosis_data && (
        <HStack>
          <h3>Диагноз</h3>
          <p>
            {card.diagnosis_data.diagnosis} (МКБ: {card.diagnosis_data.mkb})
          </p>
        </HStack>
      )}

      <Button onClick={() => navigator("/dispatcher-main/")}> Назад </Button>
    </VStack>
  );
};

export default CardDetail;
