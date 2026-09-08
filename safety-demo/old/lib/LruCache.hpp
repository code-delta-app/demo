#pragma once
#include "Cache.hpp"
#include <list>

class LruCache : public Cache {
public:
    explicit LruCache(size_t capacity) : capacity_(capacity) {}
    bool get(const std::string &key, std::string &out) const override {
        auto it = index_.find(key);
        if (it == index_.end()) return false;
        out = it->second;
        return true;
    }
    void put(const std::string &key, const std::string &value) override {
        if (index_.size() >= capacity_ && !order_.empty()) {
            index_.erase(order_.front());
            order_.pop_front();
        }
        index_[key] = value;
        order_.push_back(key);
    }
    size_t size() const override { return index_.size(); }
private:
    size_t capacity_;
    std::map<std::string, std::string> index_;
    std::list<std::string> order_;
};
