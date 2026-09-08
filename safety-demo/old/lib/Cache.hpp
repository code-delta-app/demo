#pragma once
#include <string>
#include <map>

class Cache {
public:
    virtual ~Cache() {}
    virtual bool get(const std::string &key, std::string &out) const = 0;
    virtual void put(const std::string &key, const std::string &value) = 0;
    virtual size_t size() const = 0;
};
