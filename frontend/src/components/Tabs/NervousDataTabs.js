import {
  Grid,
  GridItem,
  Text,
  Checkbox,
  HStack,
  VStack,
  Stack,
} from "@chakra-ui/react";
import { useEffect, useState } from "react";
import {
  BEHAVIOUR_CHOICES,
  REACTION_TO_LIGHT,
  PUPILS_OF_THE_EYES_CHOICES,
  SPEECH_CHOICES,
  PARALYSIS_CHOICES,
  SENSITIVE_CHOICES,
} from "../../constants/select-text";
import { SelectChoice } from "../choice.field";

const NervousDataTabs = ({ nervous, onRefSave }) => {
  const [localData, setLocalData] = useState(nervous);
  const hasSymptom =
    localData.nuchal_rigidity ||
    localData.is_kernig_symptom ||
    localData.is_brudzinski_symptom;

  useEffect(() => {
    if (nervous) {
      // Если есть симптомы, гарантированно снимаем "нет симптомов"
      if (
        nervous.nuchal_rigidity ||
        nervous.is_kernig_symptom ||
        nervous.is_brudzinski_symptom
      ) {
        setLocalData((prev) => ({
          ...prev,
          none_symptoms: false,
        }));
      } else {
        setLocalData((prev) => ({
          ...prev,
          none_symptoms: true,
        }));
      }
    }
  }, [nervous]);

  const handleChange = (field, value) => {
    const newData = {
      ...localData,
      [field]: value,
    };
    if (field === "none_symptoms" && value) {
      newData.nuchal_rigidity = false;
      newData.is_kernig_symptom = false;
      newData.is_brudzinski_symptom = false;
    } else if (
      field === "nuchal_rigidity" ||
      field === "is_kernig_symptom" ||
      field === "is_brudzinski_symptom"
    ) {
      newData.none_symptoms = false;
    }

    setLocalData(newData);
  };

  useEffect(() => {
    if (onRefSave) {
      onRefSave.current = () => localData;
    }
  }, [localData, onRefSave]);

  return (
    <Grid templateColumns="repeat(2,1fr)">
      <GridItem>
        <SelectChoice
          fieldname="Поведение"
          options={BEHAVIOUR_CHOICES}
          defaultValue={localData.behaviour}
          onChange={(e) => {
            handleChange("behaviour", e.target.value);
          }}
        />
        <SelectChoice
          fieldname="Реакция на свет"
          options={REACTION_TO_LIGHT}
          defaultValue={localData.reaction_to_light}
          onChange={(e) => {
            handleChange("reaction_to_light", e.target.value);
          }}
        />
        <SelectChoice
          fieldname="Зрачки"
          options={PUPILS_OF_THE_EYES_CHOICES}
          defaultValue={localData.pupils_of_the_eyes}
          onChange={(e) => {
            handleChange("pupils_of_the_eyes", e.target.value);
          }}
        />
        <SelectChoice
          fieldname="Речь"
          options={SPEECH_CHOICES}
          defaultValue={localData.speech}
          onChange={(e) => {
            handleChange("speech", e.target.value);
          }}
        />
        <SelectChoice
          fieldname="Парезы и параличи"
          options={PARALYSIS_CHOICES}
          defaultValue={localData.paralysis}
          onChange={(e) => {
            handleChange("paralysis", e.target.value);
          }}
        />
        <SelectChoice
          fieldname="Чувствительность"
          options={SENSITIVE_CHOICES}
          defaultValue={localData.sensitive}
          onChange={(e) => {
            handleChange("sensitive", e.target.value);
          }}
        />
      </GridItem>
      <GridItem gap={6}>
        <Checkbox
          p="10px"
          isChecked={localData.anisocoria}
          onChange={(e) => {
            handleChange("anisocoria", e.target.checked);
          }}
        >
          Анизокория
        </Checkbox>
        <Checkbox
          p="10px"
          isChecked={localData.nystagmus}
          onChange={(e) => {
            handleChange("nystagmus", e.target.checked);
          }}
        >
          Нистагм
        </Checkbox>
        <Checkbox
          p="10px"
          isChecked={localData.focal_signs}
          onChange={(e) => {
            handleChange("focal_signs", e.target.checked);
          }}
        >
          Очаговые признаки
        </Checkbox>
        <Text>Менингиальные симптомы</Text>
        <Checkbox
          p="10px"
          isDisabled={hasSymptom}
          isChecked={localData.none_symptoms}
          onChange={(e) => {
            handleChange("none_symptoms", e.target.checked);
          }}
        >
          Нет симптомов
        </Checkbox>
        <Stack pl={6} mt={1} spacing={1}>
          <Checkbox
            isDisabled={localData.none_symptoms}
            isChecked={localData.nuchal_rigidity || false}
            onChange={(e) => {
              handleChange("nuchal_rigidity", e.target.checked);
            }}
          >
            Ригидность затолочных мышц
          </Checkbox>
          <Checkbox
            isDisabled={localData.none_symptoms}
            isChecked={localData.is_kernig_symptom || false}
            onChange={(e) => {
              handleChange("is_kernig_symptom", e.target.checked);
            }}
          >
            Симптом Кернига
          </Checkbox>
          <Checkbox
            isDisabled={localData.none_symptoms}
            isChecked={localData.is_brudzinski_symptom || false}
            onChange={(e) => {
              handleChange("is_brudzinski_symptom", e.target.checked);
            }}
          >
            Симптом Брудзинского
          </Checkbox>
        </Stack>
      </GridItem>
    </Grid>
  );
};

export default NervousDataTabs;
