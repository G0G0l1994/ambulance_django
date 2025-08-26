import { useCallback, useEffect, useState, useRef } from "react";
import {
  Box,
  Textarea,
  Input,
  Text,
  HStack,
  List,
  ListItem,
} from "@chakra-ui/react";
import { getMKB } from "../../endpoints/api";
import debounce from "lodash/debounce";

const DiagnosisDataTabs = ({ diagnosis, onSaveRef }) => {
  const [localData, setLocalData] = useState(diagnosis);
  const [mkbData, setMkbData] = useState([]);
  const [searchResults, setSearchResults] = useState([]);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const containerRef = useRef(null);

  // Дебаунс для обновления данных
  const debouncedUpdate = useCallback(
    debounce((newData) => {
      setLocalData(newData);
    }, 500),
    []
  );

  // Дебаунс для поиска МКБ
  const filterMkb = useCallback(
    debounce((query) => {
      if (!query || query.length < 2) {
        setSearchResults([]);
        setShowSuggestions(false);
        return;
      }

      const lowerQuery = query.toLowerCase();
      const filtered = [];

      // Оптимизированный поиск с ограничением результатов
      for (let i = 0; i < mkbData.length && filtered.length < 50; i++) {
        const item = mkbData[i];
        if (item.code.toLowerCase().includes(lowerQuery)) {
          filtered.push(item);
        }
      }

      setSearchResults(filtered);
      setShowSuggestions(true);
    }, 300),
    [mkbData]
  );

  // Обработчик изменений для диагноза
  const handleDiagnosisChange = (value) => {
    setLocalData((prev) => {
      const newData = { ...prev, diagnosis: value };
      debouncedUpdate(newData);
      return newData;
    });
  };

  // Обработчик изменений для МКБ
  const handleMkbChange = (value) => {
    setLocalData((prev) => {
      const newData = { ...prev, mkb: value };
      debouncedUpdate(newData);
      return newData;
    });

    filterMkb(value);
  };

  // Выбор элемента МКБ
  const handleSelectMkb = (code) => {
    setLocalData((prev) => {
      const newData = { ...prev, mkb: code };
      debouncedUpdate(newData);
      return newData;
    });
    setShowSuggestions(false);
  };

  // Загрузка данных МКБ
  useEffect(() => {
    const fetchMkb = async () => {
      const data = await getMKB();
      setMkbData(data);
    };
    fetchMkb();
  }, []);

  // Обработчик клика вне области для скрытия подсказок
  useEffect(() => {
    const handleClickOutside = (e) => {
      if (containerRef.current && !containerRef.current.contains(e.target)) {
        setShowSuggestions(false);
      }
    };

    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  // Сохранение ссылки для родительского компонента
  useEffect(() => {
    if (onSaveRef) {
      onSaveRef.current = () => localData;
    }
  }, [localData, onSaveRef]);

  // Очистка дебаунсов при размонтировании
  useEffect(() => {
    return () => {
      debouncedUpdate.cancel();
      filterMkb.cancel();
    };
  }, []);

  return (
    <Box ref={containerRef}>
      <HStack mb={4}>
        <Text>Предварительный диагноз:</Text>
        <Textarea
          value={localData.diagnosis}
          onChange={(e) => handleDiagnosisChange(e.target.value)}
        />
      </HStack>

      <HStack gap="95px" position="relative">
        <Text>Код МКБ-10</Text>
        <Box position="relative" flex="1">
          <Input
            value={localData.mkb}
            onChange={(e) => handleMkbChange(e.target.value)}
            placeholder="Начните вводить код МКБ"
          />

          {showSuggestions && searchResults.length > 0 && (
            <Box
              position="absolute"
              top="100%"
              left="0"
              right="0"
              bg="white"
              border="1px solid"
              borderColor="gray.200"
              borderRadius="md"
              boxShadow="md"
              zIndex="10"
              maxH="300px"
              overflowY="auto"
            >
              <List>
                {searchResults.map((item, index) => (
                  <ListItem
                    key={index}
                    p={2}
                    _hover={{ bg: "gray.100" }}
                    cursor="pointer"
                    onClick={() => handleSelectMkb(item.code)}
                  >
                    <Text fontWeight="bold">{item.code}</Text>
                    <Text fontSize="sm">{item.name}</Text>
                  </ListItem>
                ))}
              </List>
            </Box>
          )}
        </Box>
      </HStack>
    </Box>
  );
};

export default DiagnosisDataTabs;
